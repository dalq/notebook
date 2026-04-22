import torch
import torch.nn as nn
from llmsFromScratch.ch03_attention.MultiHeadAttention import MultiHeadAttention
from llmsFromScratch.ch04_gpt.LayNorm_Glue_FFN import FeedForward, LayerNorm, GPT_CONFIG_124M


# 多头注意力、层归一化、dropout、前馈层和GELU激活函数
class TransformerBlock(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.att = MultiHeadAttention(
            d_in = cfg["emb_dim"],
            d_out = cfg["emb_dim"],
            context_length = cfg["context_length"],
            dropout = cfg["drop_rate"],
            num_heads = cfg["n_heads"],
            qkv_bias= cfg["qkv_bias"]
        )
        self.ff = FeedForward(cfg)
        self.norm1 = LayerNorm(cfg["emb_dim"])
        self.norm2 = LayerNorm(cfg["emb_dim"])
        self.drop_shortcut = nn.Dropout(cfg["drop_rate"])

    def forward(self, x):
        # Shortcut connection for attention block
        short_cut = x
        x = self.norm1(x)
        x = self.att(x)
        x = self.drop_shortcut(x)
        x = x + short_cut

        # Shortcut connection for feed forward block
        short_cut = x
        x = self.norm2(x)
        x = self.ff(x)
        x = self.drop_shortcut(x)
        x = x + short_cut

        return x

if __name__ == '__main__':
    torch.manual_seed(123)
    # [batch_size, num_tokens, emb_dim]
    x = torch.randn(2, 4, 768)
    block = TransformerBlock(GPT_CONFIG_124M)
    output = block(x)

    print("Input shape:", x.shape)
    print("Output shape:", output.shape)