import torch
import torch.nn as nn
from llmsFromScratch.ch03_attention.AttentionWithTrainedWeight import SelfAttention_V2

# 相较于SelfAttention_V2,增加了掩码机制,以及dropout
class CausalAttention(nn.Module):
    def __init__(self, d_in, d_out, context_length, dropout, qkv_bias=False):
        super().__init__()
        self.W_query = nn.Linear(d_in, d_out, bias=qkv_bias)
        self.W_key = nn.Linear(d_in, d_out, bias=qkv_bias)
        self.W_value = nn.Linear(d_in, d_out, bias=qkv_bias)
        self.dropout = nn.Dropout(dropout)
        # 只要是“模型的一部分，但不是可学习参数”的张量，就用 register_buffer
        self.register_buffer("mask", torch.triu(torch.ones(context_length, context_length), diagonal=1))

    def forward(self, x):
        b, num_tokens, d_in = x.shape
        keys = self.W_key(x)
        queries = self.W_query(x)
        values = self.W_value(x)

        # .T只能转置2D张量,3D张量需要用transpose指定要交换哪两个维度(从0开始算)
        atten_scores = queries @ keys.transpose(1, 2)
        # PyTorch 中，方法名末尾带 _ 的，表示直接修改原张量本身，不会创建新张量
        # 在 mask 为 True 的位置，填入 -inf
        # "按掩码原地填充" —— 在 mask 为 True 的位置，直接把原张量的值改成指定值（这里是 -inf）
        atten_scores.masked_fill_(self.mask.bool()[:num_tokens, :num_tokens], -torch.inf)
        atten_weights = torch.softmax(atten_scores / keys.shape[-1] ** 0.5, dim=-1)
        atten_weights = self.dropout(atten_weights)

        context_vec = atten_weights @ values
        return context_vec



if __name__ == '__main__':
    # input embedding之后的向量,假设embedding维度=3
    inputs = torch.tensor(
        [[0.43, 0.15, 0.89],  # Your     (x^1)
         [0.55, 0.87, 0.66],  # journey  (x^2)
         [0.57, 0.85, 0.64],  # starts   (x^3)
         [0.22, 0.58, 0.33],  # with     (x^4)
         [0.77, 0.25, 0.10],  # one      (x^5)
         [0.05, 0.80, 0.55]]  # step     (x^6)
    )

    d_in = inputs.shape[1]
    d_out = 2
    sa_v2 = SelfAttention_V2(d_in, d_out)
    queries = sa_v2.W_query(inputs)
    keys = sa_v2.W_key(inputs)
    values = sa_v2.W_value(inputs)
    attn_scores = queries @ keys.T
    attn_weights = torch.softmax(attn_scores / keys.shape[-1] ** 0.5, dim=-1)
    print(attn_weights)

    context_length = attn_scores.shape[0]
    # 用于提取输入张量的下三角部分，并将上三角置零
    # 是triu而不是trill
    mask_simple = torch.triu(torch.ones(context_length, context_length))
    print(mask_simple)
    # 掩码矩阵和注意力权重矩阵相乘，使对角线上方的值变为0
    masked_simple = attn_weights * mask_simple
    print(masked_simple)
    # 重新归一化,这次用的是:每行中的每个元素除以每行中的和
    row_sums = masked_simple.sum(dim=-1, keepdim=True)
    masked_simple_norm = masked_simple / row_sums
    print(masked_simple_norm)

    # 🔥更有效的方法是在应用softmax函数之前将注意力分数用负无穷大值进行掩码
    mask = torch.triu(torch.ones(context_length, context_length), diagonal=1)
    masked = attn_scores.masked_fill(mask.bool(), -torch.inf)
    print(masked)
    attn_weights = torch.softmax(masked / keys.shape[-1] ** 0.5, dim=-1)
    print(attn_weights)
    context_vec = attn_weights @ values
    print(context_vec.shape)

    # 🔥将操作封装为CausalAttention
    batch = torch.stack((inputs, inputs), dim=0) # input: 6 * 3
    print('batch.shape: ', batch.shape)  #(2, 6, 3), 2:batch_size= 2,2个输入样本; 6:num_tokens,每个输入6个token; 3:embedding dimension,每个token的嵌入维度
    torch.manual_seed(333)
    context_length = batch.shape[1]
    ca = CausalAttention(d_in, d_out, context_length, 0.0)
    context_vecs = ca(batch)
    print('context_vecs.shape: ', context_vecs.shape)