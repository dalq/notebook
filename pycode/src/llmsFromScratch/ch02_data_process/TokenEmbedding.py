import torch
from SlideWindowSampling import  create_dataloader_v1


if __name__ == '__main__':
    input_ids = torch.tensor([2, 3, 5, 1])
    vocab_size = 6
    output_dim = 3

    torch.manual_seed(123)
    embedding_layer = torch.nn.Embedding(vocab_size, output_dim)
    print(embedding_layer.weight)

    # token index = 3,去嵌入矩阵第4行找对应的向量值
    print(embedding_layer(torch.tensor([3])))


    # 1. 读取文本数据
    with open("the-verdict.txt", "r", encoding="utf-8") as f:
        raw_text = f.read()
    max_length = 4
    # 2. 数据加载器,利用tokenizer.encode完成了词元切分,查表得到id,以及滑动窗口采样,按照batch分批
    dataloader = create_dataloader_v1(
        raw_text, batch_size=8, max_length=max_length,
        stride=max_length, shuffle=False
    )
    data_iter = iter(dataloader)
    inputs, targets = next(data_iter)
    # 词元ID张量的维度为8×4，这表明数据批次包含8个文本样本，每个样本由4个词元组成。
    print("Token IDs:\n", inputs)
    print("\nInputs shape:\n", inputs.shape)
    # 3.词元ID嵌入256维的向量中
    # 输入的词元编码为256维的向量表示
    vocab_size = 50257
    output_dim = 256
    token_embedding_layer = torch.nn.Embedding(vocab_size, output_dim)
    token_embeddings = token_embedding_layer(inputs) # inputs: 8 * 4
    # 每个批次 8 with 4 tokens ,结果会是 8 x 4 x 256 tensor:
    print(token_embeddings.shape) # 8 * 4 * 256
    # 4.位置编码
    context_length = max_length
    pos_embedding_layer = torch.nn.Embedding(context_length, output_dim)
    # arange函数生成底层的序列
    # torch.nn.Embedding 的规律是：输出形状 = 输入形状 + [output_dim]
    pos_embeddings = pos_embedding_layer(torch.arange(max_length)) # inputs: 4,
    # Transformer 的注意力机制关心的是词与词之间的相对关系，而不是它们在整篇文章里的绝对位置
    # 位置编码就是"本页的第几行"，不是"全书的第几行"
    print("pos embedding shape: ", pos_embeddings.shape)
    input_embeddings = token_embeddings + pos_embeddings
    print("token embedding + pos embedding shape:", input_embeddings.shape)
