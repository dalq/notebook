# 带可训练权重的自注意力机制
import torch
# nn.Module是PyTorch模型的一个基本构建块，它为模型层的创建和管理提供了必要的功能。
import torch.nn as nn


class SelfAttention_V1(nn.Module):
    def __init__(self, d_in, d_out):
        super().__init__()
        self.W_query = nn.Parameter(torch.rand(d_in, d_out))
        self.W_key = nn.Parameter(torch.rand(d_in, d_out))
        self.W_value = nn.Parameter(torch.rand(d_in, d_out))
    def forward(self, x):
        keys = x @ self.W_key
        queries = x @ self.W_query
        values = x @ self.W_value
        attn_scores = queries @ keys.T
        attn_weights = torch.softmax(
            attn_scores / keys.shape[-1] ** 0.5, dim=-1
        )
        # attention分数权重(q乘以v再归一化)乘以v
        context_vec = attn_weights @ values
        return context_vec

# 升级为pytorch的全连接/线性层
class SelfAttention_V2(nn.Module):
    def __init__(self, d_in, d_out, qkv_bias=False):
        super().__init__()
        self.W_query = nn.Linear(d_in, d_out, bias=qkv_bias)
        self.W_key = nn.Linear(d_in, d_out, bias=qkv_bias)
        self.W_value = nn.Linear(d_in, d_out, bias=qkv_bias)
    def forward(self, x):
        keys = self.W_key(x)
        queries = self.W_query(x)
        values = self.W_value(x)
        attn_scores = queries @ keys.T
        attn_weights = torch.softmax(
            attn_scores / keys.shape[-1] ** 0.5, dim=-1
        )
        # attention分数权重(q乘以v再归一化)乘以v
        context_vec = attn_weights @ values
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

    # 这里的x_2本身不是query了,需要和W_q相乘后才是query
    x_2 = inputs[1]
    d_in = inputs.shape[1]
    d_out = 2

    # 初始化W_q,W_k,W_v
    torch.manual_seed(123)
    W_query = torch.nn.Parameter(torch.rand(d_in, d_out), requires_grad=False) #减少输出信息,例如不参与反向传播
    W_key = torch.nn.Parameter(torch.rand(d_in, d_out), requires_grad=False)
    W_value = torch.nn.Parameter(torch.rand(d_in, d_out), requires_grad=False)
    query_2 = x_2 @ W_query
    key_2 = x_2 @ W_key
    value_2 = x_2 @ W_value
    print('query_2:', query_2)

    # 计算出所有的key向量和value向量
    keys = inputs @ W_key
    values = inputs @ W_value
    print("keys.shape:", keys.shape) # 6 * 3 --> 6 * 2
    print("values.shape:", values.shape) # 6 * 3 --> 6 * 2

    # x_2对x_2的key的注意力分数,也即w_22
    key_2 = keys[1]
    attn_score_22 = query_2.dot(key_2)
    print(attn_score_22)
    # x_2对所有x的key的注意力分数,也即w_2
    attn_score_2 = query_2 @ keys.T
    print(attn_score_2)

    # 将注意力分数进行缩放成为权重
    # x_2对所有词的 attention 权重矩阵
    d_k = keys.shape[1]
    # 归一化是为了避免梯度过小，从而提升训练性能
    # 嵌入维度的平方根进行缩放,避免梯度消失和爆炸
    attn_weights_2 = torch.softmax(attn_score_2 / d_k ** 0.5, dim=-1)
    print(attn_weights_2)

    # 计算上下文向量z^2
    context_vec_2 = attn_weights_2 @ values
    print(context_vec_2)

    # 上面计算了很多次,此时种子状态已经被消耗了很多，生成的随机数完全不同
    torch.manual_seed(123)
    sa_v1 = SelfAttention_V1(d_in, d_out)
    print(sa_v1(inputs))

    # 上面计算了很多次,此时种子状态已经被消耗了很多，生成的随机数完全不同
    torch.manual_seed(789)
    sa_v2 = SelfAttention_V2(d_in, d_out)
    print(sa_v2(inputs))