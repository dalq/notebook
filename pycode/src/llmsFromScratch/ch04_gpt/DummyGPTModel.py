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
        self.trf_blocks = nn.Sequential(
            *[DummyTransformerBlock(cfg) for _ in range(cfg["n_layers"])])

        # LayerNorm层归一化待实现
        self.final_norm = DummyLayerNorm(cfg["emb_dim"])
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


class DummyTransformerBlock(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        # A simple placeholder

    def forward(self, x):
        # This block does nothing and just returns its input.
        return x

# 提高神经网络训练的稳定性和效率
# 让每一层的输出数值保持稳定，防止训练过程中数值变得过大或过小
# 会用在两个地方:每个 Transformer Block 内部,以及最后一层
class DummyLayerNorm(nn.Module):
    def __init__(self, normalized_shape, eps=1e-5):
        super().__init__()
        # The parameters here are just to mimic the LayerNorm interface.

    def forward(self, x):
        # This layer does nothing and just returns its input.
        return x

if __name__ == '__main__':
    tokenizer = tiktoken.get_encoding("gpt2")

    batch = []

    txt1 = "Every effort moves you"
    txt2 = "Every day holds a"

    batch.append(torch.tensor(tokenizer.encode(txt1)))
    batch.append(torch.tensor(tokenizer.encode(txt2)))
    batch = torch.stack(batch, dim=0)
    print(batch)
    torch.manual_seed(123)
    model = DummyGPTModel(GPT_CONFIG_124M)
    # 模型的输出（通常称为logits）
    logits = model(batch)
    # 虽然嵌入层embedding是768维,但是最后经过线性变换为了词表的50257维
    print("Output shape:", logits.shape) #两个批次, 每个批次由4个token, 每个token是50257维的向量
    # 因为模型最终要预测下一个词是什么。词表里一共有 50257 个词，所以输出的 50257 维向量中，每一维代表对应词的"得分"（logits）。
    # 得分最高的那个位置对应的词，就是模型预测的下一个词
    # 把 768 维的隐藏状态映射到 50257 维的词表空间
    print(logits)
