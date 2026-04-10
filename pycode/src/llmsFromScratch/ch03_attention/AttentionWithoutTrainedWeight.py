import torch

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

    # 计算x^2与所有x的注意力(静态的,通过点击得来的)
    query = inputs[1]
    attn_scores_2 = torch.empty(inputs.shape[0])
    for i, x_i in enumerate(inputs):
        attn_scores_2[i] = torch.dot(x_i, query)
    # 归一化
    attn_weights_2 = torch.softmax(attn_scores_2, dim=0)
    print('x^2与所有x的注意力并归一化:', attn_weights_2)
    # 上下文向量z^2,也就是所有输入向量x^1到x^6按attn_weights_2权重加权和
    context_vec_2 = torch.zeros(query.shape)
    for i, x_i in enumerate(inputs):
        context_vec_2 += attn_weights_2[i] * x_i
    print('上下文向量z^2:',context_vec_2)


    # 计算所有上下文向量
    # attn_scores = torch.empty(6, 6)
    # for i, x_i in enumerate(inputs):
    #     for j, x_j in enumerate(inputs):
    #         attn_scores[i, j] = torch.dot(x_i, x_j)
    # print(attn_scores)
    attn_scores = inputs @ inputs.T # 使用矩阵乘法替代较为慢的双层for循环
    print('attention scores:', attn_scores)
    # dim设置为-1表示让softmax函数在attn_scores张量的最后一个维度上进行归一化。
    # 如果attn_scores是一个二维张量（比如形状为［行, 列］），那么每行的值总和为1。
    attn_weights = torch.softmax(attn_scores, dim=-1)
    print('attention weights after softmax:', attn_weights)
    # 所有input乘以所有权重
    all_context_vecs = attn_weights @ inputs
    print('context vector after attention:', all_context_vecs)

    # 验证: context_vec_2 应该与 all_context_vecs 的第二个元素相等
    assert torch.allclose(context_vec_2, all_context_vecs[1]), \
        f"不相等! context_vec_2={context_vec_2}, all_context_vecs[1]={all_context_vecs[1]}"
    print("✅ 验证通过: context_vec_2 == all_context_vecs[1]")
