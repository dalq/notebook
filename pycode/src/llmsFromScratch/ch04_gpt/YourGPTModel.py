import torch
import torch.nn as nn
import tiktoken
from ch04_gpt.TransformerBlock import TransformerBlock
from ch04_gpt.LayNorm_Glue_FFN import LayerNorm, GPT_CONFIG_124M

class GPTModel(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.tok_emb = nn.Embedding(cfg["vocab_size"], cfg["emb_dim"])
        self.pos_emb = nn.Embedding(cfg["context_length"], cfg["emb_dim"])
        self.drop_emb = nn.Dropout(cfg["drop_rate"])

        self.trf_blocks = nn.Sequential(
            *[TransformerBlock(cfg) for _ in range(cfg["n_layers"])])

        self.final_norm = LayerNorm(cfg["emb_dim"])

        self.out_head = nn.Linear(
            cfg["emb_dim"], cfg["vocab_size"], bias=False
        )

    def forward(self, in_idx):
        batch_size, seq_len = in_idx.shape
        tok_embeds = self.tok_emb(in_idx)
        pos_embeds = self.pos_emb(torch.arange(seq_len, device=in_idx.device))
        x = tok_embeds + pos_embeds  # Shape [batch_size, num_tokens, emb_size]
        x = self.drop_emb(x)
        x = self.trf_blocks(x)
        x = self.final_norm(x)
        logits = self.out_head(x)
        return logits


def generate_text_simple(model, idx, max_new_tokens, context_size):
    """
    自回归文本生成：每次预测下一个 token，追加到序列末尾，循环 max_new_tokens 次。
    
    工作流程（以 "Hello, I am" 生成 3 个新 token 为例）：
      第1轮: [Hello, ,, I, am]         → 模型预测下一个词 → [Hello, ,, I, am, a]
      第2轮: [Hello, ,, I, am, a]      → 模型预测下一个词 → [Hello, ,, I, am, a, student]
      第3轮: [Hello, ,, I, am, a, student] → 模型预测下一个词 → [Hello, ,, I, am, a, student, .]
    
    Args:
        model: GPTModel 实例
        idx: 初始 token 索引序列，shape 为 (batch_size, n_tokens)
        max_new_tokens: 要生成的新 token 数量
        context_size: 模型支持的最大上下文长度（超出部分会被截断）
    """
    for _ in range(max_new_tokens):
        # 如果当前序列超过模型支持的上下文长度，只保留最后 context_size 个 token
        # 例如：context_size=5，序列长度=10，则只取最后 5 个 token 作为输入
        idx_cond = idx[:, -context_size:]

        # 前向推理，不需要计算梯度（推理阶段不做反向传播）
        with torch.no_grad():
            logits = model(idx_cond)  # (batch, n_tokens, vocab_size)

        # 只取最后一个位置的输出——因为自回归模型中，最后一个位置的输出就是"下一个 token"的预测
        # (batch, n_tokens, vocab_size) → (batch, vocab_size)
        logits = logits[:, -1, :]

        # 转换为概率分布（其实这里用 argmax，softmax 不是必须的，但语义更清晰）
        probas = torch.softmax(logits, dim=-1)  # (batch, vocab_size)

        # 贪心解码：取概率最大的 token 作为预测结果
        idx_next = torch.argmax(probas, dim=-1, keepdim=True)  # (batch, 1)

        # 将新预测的 token 拼接到序列末尾，作为下一轮的输入
        idx = torch.cat((idx, idx_next), dim=1)  # (batch, n_tokens+1)

    return idx

if __name__ == '__main__':
    tokenizer = tiktoken.get_encoding("gpt2")

    batch = []

    txt1 = "Every effort moves you"
    txt2 = "Every day holds a"

    batch.append(torch.tensor(tokenizer.encode(txt1)))
    batch.append(torch.tensor(tokenizer.encode(txt2)))
    batch = torch.stack(batch, dim=0)

    torch.manual_seed(123)
    x = torch.randn(2, 4, 768)# [batch_size, num_tokens, emb_dim]
    model = GPTModel(GPT_CONFIG_124M)

    out = model(batch)
    print("Input batch:\n", batch) #
    print("\nOutput shape:", out.shape) # [2, 4, 50257]
    # 传入两个输入文本，每个文本有4个词元，维度50257相当于分词器的词汇量
    print(out)

    # 推理:
    start_context = "Hello, I am"
    encoded = tokenizer.encode(start_context)
    print("encoded:", encoded)
    encoded_tensor = torch.tensor(encoded).unsqueeze(0)
    print("encoded_tensor.shape:", encoded_tensor.shape)
    model.eval()  # disable dropout
    out = generate_text_simple(
        model=model,
        idx=encoded_tensor,
        max_new_tokens=6,
        context_size=GPT_CONFIG_124M["context_length"]
    )
    print("Output:", out)
    print("Output length:", len(out[0]))
    decoded_text = tokenizer.decode(out.squeeze(0).tolist())
    print(decoded_text)