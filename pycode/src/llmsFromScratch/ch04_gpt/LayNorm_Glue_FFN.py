import torch
import torch.nn as nn
import tiktoken

GPT_CONFIG_124M = {
    "vocab_size": 50257,    # Vocabulary size
    "context_length": 1024, # Context length
    "emb_dim": 768,         # Embedding dimension
    "n_heads": 12,          # Number of attention heads
    "n_layers": 12,         # Number of layers
    "drop_rate": 0.1,       # Dropout rate
    "qkv_bias": False       # Query-Key-Value bias
}

class DummyGPTModel(nn.Module):
    # 配置信息通过一个Python字典config传入。
    def __init__(self, cfg):
        super().__init__()
        self.tok_emb = nn.Embedding(cfg["vocab_size"], cfg["emb_dim"])
        self.pos_emb = nn.Embedding(cfg["context_length"], cfg["emb_dim"])
        self.drop_emb = nn.Dropout(cfg["drop_rate"])

        # TransformerBlock待实现
        # self.trf_blocks = nn.Sequential(
        #     *[DummyTransformerBlock(cfg) for _ in range(cfg["n_layers"])])

        # LayerNorm层归一化待实现
        self.final_norm = LayerNorm(cfg["emb_dim"])
        # 输入 token ID:  (2, 4)           → 2个批次，每个4个token
        #     ↓ embedding
        # 嵌入向量:       (2, 4, 768)      → 每个token变成768维向量
        #     ↓ transformer blocks + norm
        # 隐藏状态:       (2, 4, 768)      → 维度不变，还是768
        #     ↓ out_head: nn.Linear(768, 50257)
        # logits:         (2, 4, 50257)    → 每个token变成50257维
        self.out_head = nn.Linear(
            cfg["emb_dim"], cfg["vocab_size"], bias=False # 全连接层,从输入维度 768 映射到输出维度 50257。
        )

    def forward(self, in_idx):
        batch_size, seq_len = in_idx.shape
        tok_embeds = self.tok_emb(in_idx)
        pos_embeds = self.pos_emb(torch.arange(seq_len, device=in_idx.device))
        x = tok_embeds + pos_embeds
        x = self.drop_emb(x)
        x = self.trf_blocks(x)
        x = self.final_norm(x)
        logits = self.out_head(x)
        return logits

# 提高神经网络训练的稳定性和效率
# 让每一层的输出数值保持稳定，防止训练过程中数值变得过大或过小
# 会用在两个地方:每个 Transformer Block 内部,以及最后一层
class LayerNorm(nn.Module):
    def __init__(self, emb_dim):
        super().__init__()
        self.eps = 1e-5
        self.scale = nn.Parameter(torch.ones(emb_dim))
        self.shift = nn.Parameter(torch.zeros(emb_dim))

    # transformer 选择LN:沿 特征维度（即每个 token 的 embedding 向量内部）做归一化，确保每个 token 自身的数值分布稳定。
        # | --> 看的是一个样本内部所有特征 → "这个 token 自己内部要平衡"
    # CNN 选择BN:所有样本的同一通道要统一标准. 看的是所有样本的同一个特征 → "所有图片的红色通道要统一"
    def forward(self, x):
        mean = x.mean(dim=-1, keepdim=True)
        var = x.var(dim=-1, keepdim=True, unbiased=False)
        norm_x = (x - mean) / torch.sqrt(var + self.eps)
        return self.scale * norm_x + self.shift

# 更为复杂但更平滑的激活函数
class GELU(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return 0.5 * x * (1 + torch.tanh(
            torch.sqrt(torch.tensor(2.0 / torch.pi)) *
            (x + 0.044715 * torch.pow(x, 3))
        ))

# 小型神经网络模块,前馈神经网络
class FeedForward(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(cfg["emb_dim"], 4 * cfg["emb_dim"]), # 先展开到高维空间学习信息
            GELU(), # 应用非线性GELU激活
            nn.Linear(4 * cfg["emb_dim"], cfg["emb_dim"]), # 然后再回到低维空间
        )

    def forward(self, x):
        return self.layers(x)

if __name__ == '__main__':
    torch.manual_seed(123)
    # create 2 training examples with 5 dimensions (features) each
    batch_example = torch.randn(2, 5)
    # 关闭 PyTorch 的科学计数法
    torch.set_printoptions(sci_mode=False)

    # 普通层：线性变换 + ReLU激活
    layer = nn.Sequential(nn.Linear(5, 6), nn.ReLU())
    out = layer(batch_example)
    mean = out.mean(dim=-1, keepdim=True)
    var = out.var(dim=-1, keepdim=True)
    print("Mean:\n", mean)
    print("Variance:\n", var)

    # 归一化层：均值归零、方差归一
    layer_norm = LayerNorm(emb_dim=5)
    out_ln = layer_norm(batch_example)
    mean = out_ln.mean(dim=-1, keepdim=True)
    var = out_ln.var(dim=-1, unbiased=False, keepdim=True)

    print("Mean:\n", mean)
    print("Variance:\n", var)
