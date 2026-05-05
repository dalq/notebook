import json
import os
import requests
import torch
from torch.utils.data import Dataset
import tiktoken


def download_and_load_file(file_path, url):
    if not os.path.exists(file_path):
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        text_data = response.text
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text_data)

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data

def format_input(entry):
    instruction_text = (
        f"Below is an instruction that describes a task. "
        f"Write a response that appropriately completes the request."
        f"\n\n### Instruction:\n{entry['instruction']}"
    )

    input_text = (
        f"\n\n### Input:\n{entry['input']}" if entry['input'] else ""
    )

    return instruction_text + input_text

class InstructionDataSet(Dataset):
    def __init__(self, data, tokenizer):
        self.data = data

        self.encoded_texts = []
        for entry in data:
            instruction_plus_input = format_input(entry)
            response_text = f"\n\n### Response:\n{entry['output']}"
            full_text = instruction_plus_input + response_text
            self.encoded_texts.append(
                tokenizer.encode(full_text)
            )

    def __getitem__(self, index):
        return self.encoded_texts[index]

    def __len__(self):
        return len(self.data)


# 填充<|endoftext|>
def custom_collate_draft_1(batch, pad_token_id = 50256, device = "cpu"):
    # 找到批次中最长的序列
    batch_max_length = max(len(item)+1 for item in batch)
    inputs_lst = []

    for item in batch:
        new_item = item.copy()
        new_item += [pad_token_id]
        padded = new_item + [pad_token_id] *(batch_max_length - len(new_item))
        # remove the extra padded token
        inputs = torch.tensor(padded[:-1])
        inputs_lst.append(inputs)

    # 张量
    inputs_tensor = torch.stack(inputs_lst).to(device)
    return inputs_tensor


# 还需要生成与输入词元ID批次对应的目标词元ID
def custom_collate_draft_2(batch, pad_token_id = 50256, device = "cpu"):
    # 找到批次中最长的序列
    batch_max_length = max(len(item)+1 for item in batch)
    inputs_lst, targets_lst = [], []

    for item in batch:
        new_item = item.copy()
        new_item += [pad_token_id]
        padded = new_item + [pad_token_id] *(batch_max_length - len(new_item))
        # 截断输入的最后一个次元
        inputs = torch.tensor(padded[:-1])
        # 向左移动一个位置得到目标词元们
        targets = torch.tensor(padded[1:])
        inputs_lst.append(inputs)
        targets_lst.append(targets)

    # 张量
    inputs_tensor = torch.stack(inputs_lst).to(device)
    targets_tensor = torch.stack(targets_lst).to(device)
    return inputs_tensor, targets_tensor

# 最终版,把*targets* padding 位置的 label 设为 -100 让 loss 忽略它们，但保留第一个 padding 当作 EOS 让模型学会"何时停止"。
def custom_collate_fn(batch, pad_token_id=50256, ignore_index=-100, allowed_max_length=None, device="cpu"):
    # 这个 +1 是给结尾的 EOS（<|endoftext|> = 50256）预留的
    batch_max_length = max(len(item)+1 for item in batch)
    inputs_lst, targets_lst = [], []

    for item in batch:
        new_item = item.copy()
        new_item += [pad_token_id]
        padded = new_item + [pad_token_id] *(batch_max_length - len(new_item))
        # 截断输入的最后一个次元
        inputs = torch.tensor(padded[:-1])
        # 向左移动一个位置得到目标词元们
        targets = torch.tensor(padded[1:])

        # 把目标序列中除第一个填充词元外的所有填充词元全部替换为ingore_index
        mask = targets == pad_token_id # 逐元素比较，得到一个布尔 tensor, 类似:[False, False, False, True, True, True]
        indices = torch.nonzero(mask).squeeze() # nonzero返回所有 True 的下标, 类似: [[3], [4], [5]]
        if indices.numel() > 1: # squeeze() 把多余的维度去掉，变成一维
            targets[indices[1:]] = ignore_index # 跳过第一个padding下标，用高级索引一次性把这些位置全改成 -100

        # 可选: 截断为指定的最大序列长度
        if allowed_max_length is not None:
            inputs = inputs[:allowed_max_length]
            targets = targets[:allowed_max_length]


        inputs_lst.append(inputs)
        targets_lst.append(targets)

    # 张量
    inputs_tensor = torch.stack(inputs_lst).to(device)
    targets_tensor = torch.stack(targets_lst).to(device)
    return inputs_tensor, targets_tensor


if __name__ == '__main__':
    file_path = "instruction-data.json"
    url = (
        "https://raw.githubusercontent.com/rasbt/LLMs-from-scratch"
        "/main/ch07/01_main-chapter-code/instruction-data.json"
    )
    data = download_and_load_file(file_path, url)
    print("Number of entries:", len(data))

    model_input = format_input(data[50])
    desired_output = f"\n\n### Response:\n{data[50]['output']}"
    print(model_input + desired_output)

    tokenizer = tiktoken.get_encoding("gpt2")
    # 50256
    print(tokenizer.encode("<|endoftext|>", allowed_special={"<|endoftext|>"}))

    inputs_1, inputs_2, inputs_3 = [0, 1, 2, 3, 4], [5, 6], [7, 8, 9]
    batch = (inputs_1,inputs_2,inputs_3)
    print(custom_collate_draft_1(batch)) #填充padding

    inputs, targets = custom_collate_draft_2(batch) # 同时输出inputs和targets
    print('同时返回输入和目标批次',inputs)
    print(targets)

    inputs, targets = custom_collate_fn(batch)  # 对应位置插入了词元ID-100
    print('对应位置插入了词元ID-100', inputs)
    print(targets)