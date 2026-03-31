import tiktoken
import torch
from torch.utils.data import Dataset, DataLoader
from SimpleTokenizer import SimpleTokenizerV2

class GPTDatasetV1(Dataset):
    def __init__(self, text, tokenizer, max_length, stride):
        self.input_ids = []
        self.target_ids = []

        token_ids = tokenizer.encode(text, allowed_special={"<|endoftext|>"})
        assert len(token_ids) > max_length, "Number of tokenized inputs must at least be equal to max_length+1"

        for i in range(0, len(token_ids) - max_length, stride):
            input_chunk = token_ids[i:i + max_length]
            target_chunk = token_ids[i + 1: i + max_length + 1]
            self.input_ids.append(torch.tensor(input_chunk))
            self.target_ids.append(torch.tensor(target_chunk))

    def __len__(self):
        return len(self.input_ids)

    def __getitem__(self, idx):
        return self.input_ids[idx], self.target_ids[idx]

def create_dataloader_v1(txt, batch_size=4, max_length=256,
                         stride=128, shuffle=True, drop_last=True, # stride滑动步长
                         num_workers=0):
    # Initialize the tokenizer
    tokenizer = tiktoken.get_encoding("gpt2")

    # Create dataset
    dataset = GPTDatasetV1(txt, tokenizer, max_length, stride)

    # Create dataloader
    dataloader = DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=shuffle,
        drop_last=drop_last, # 最后一批小于batch_size，是否丢弃最后一批
        num_workers=num_workers # CPU
    )

    return dataloader

if __name__ == '__main__':
    with open("the-verdict.txt", "r", encoding="utf-8") as f:
        raw_text = f.read()

    # tiktoken，它基于Rust的源代码非常高效地实现了BPE分词算法
    tokenizer = tiktoken.get_encoding("gpt2")
    enc_text = tokenizer.encode(raw_text)
    print(len(enc_text))

    enc_sample = enc_text[50:]
    context_size = 4
    for i in range(1, context_size + 1):
        context = enc_sample[:i]
        desired = enc_sample[i]
        print(context, "---->", desired, "【" ,tokenizer.decode(context), "---->", tokenizer.decode([desired]), "】")

    # create_dataloader_v1
    dataloader = create_dataloader_v1(
        raw_text, batch_size=1, max_length=4, stride=1, shuffle=False
    )
    data_iter = iter(dataloader)
    first_batch = next(data_iter)
    print(first_batch) # 第一个张量存储输入词元ID，第二个张量存储目标词元ID。由于max_length被设置为4，因此这两个张量各自包含4个词元ID。

    # 增大batch_size
    dataloader = create_dataloader_v1(
        raw_text, batch_size=8, max_length=4, stride=4, shuffle=False
    )
    data_iter = iter(dataloader)
    inputs, targets = next(data_iter)
    print('整篇文章编码后的一个完整的 ID 列表:', enc_text[0:200])
    print("batch_size=8 Inputs:\n", inputs)
    print("\n batch_size=8 Targets:\n", targets)