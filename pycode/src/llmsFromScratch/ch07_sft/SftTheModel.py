import tiktoken
import torch
from torch.utils.data import Dataset, DataLoader
import time

from gpt_download import download_and_load_gpt2
from llmsFromScratch.ch04_gpt.YourGPTModel import GPTModel
from llmsFromScratch.ch05_pre_training.TrainingLLM import calc_loss_loader, train_model_simple
from llmsFromScratch.ch05_pre_training.WeightsDownload import load_weights_into_gpt
from llmsFromScratch.ch07_sft.DataSetPrepare import custom_collate_fn, download_and_load_file, format_input, InstructionDataSet
from llmsFromScratch.ch07_sft.ModelDownload import BASE_CONFIG, model_configs, CHOOSE_MODEL

if __name__ == '__main__':
    # dict内置的合并方法
    BASE_CONFIG.update(model_configs[CHOOSE_MODEL])
    model_size = CHOOSE_MODEL.split(" ")[-1].lstrip("(").rstrip(")")

    # 主备对调：国内访问 Backblaze（backup_base_url）通常比 Azure Blob（base_url）快很多
    settings, params = download_and_load_gpt2(
        model_size=model_size,
        models_dir="gpt2"
    )

    model = GPTModel(BASE_CONFIG)
    load_weights_into_gpt(model, params)
    model.eval()
    # 上面都是前一小节的代码

    # 判断当前芯片
    if torch.cuda.is_available():
        device = torch.device("cuda")
    elif torch.backends.mps.is_available():
        # Use PyTorch 2.9 or newer for stable mps results
        major, minor = map(int, torch.__version__.split(".")[:2])
        if (major, minor) >= (2, 9):
            device = torch.device("mps")
        else:
            device = torch.device("cpu")
    else:
        device = torch.device("cpu")
    print("Device:", device)

    # 数据加载start
    file_path = "instruction-data.json"
    url = (
        "https://raw.githubusercontent.com/rasbt/LLMs-from-scratch"
        "/main/ch07/01_main-chapter-code/instruction-data.json"
    )
    data = download_and_load_file(file_path, url)
    print("Number of entries:", len(data))
    train_portion = int(len(data) * 0.85)  # 85% for training
    test_portion = int(len(data) * 0.1)  # 10% for testing
    val_portion = len(data) - train_portion - test_portion  # Remaining 5% for validation
    train_data = data[:train_portion]
    test_data = data[train_portion: train_portion + test_portion]
    val_data = data[train_portion + test_portion:]
    # 初始化数据加载器
    num_workers = 0
    batch_size = 8
    torch.manual_seed(123)
    tokenizer = tiktoken.get_encoding("gpt2")
    train_dataset = InstructionDataSet(train_data, tokenizer)
    train_loader = DataLoader(
        train_dataset,
        batch_size=batch_size,
        collate_fn=custom_collate_fn,
        shuffle=True,
        drop_last=True,
        num_workers=num_workers
    )

    test_dataset = InstructionDataSet(test_data, tokenizer)
    test_loader = DataLoader(
        test_dataset,
        batch_size=batch_size,
        collate_fn=custom_collate_fn,
        shuffle=False,
        drop_last=False,
        num_workers=num_workers
    )

    val_dataset = InstructionDataSet(val_data, tokenizer)
    val_loader = DataLoader(
        val_dataset,
        batch_size=batch_size,
        collate_fn=custom_collate_fn,
        shuffle=False,
        drop_last=False,
        num_workers=num_workers
    )
    ## 数据加载end

    model.to(device)
    torch.manual_seed(123)
    with torch.no_grad():
        train_loss = calc_loss_loader(train_loader, model, device, num_batches=5)
        val_loss = calc_loss_loader(val_loader, model, device, num_batches=5)

    # 初始的损失值
    print("Training loss:", train_loss)
    print("Validation loss:", val_loss)

    # 开始进行指令微调:
    start_time = time.time()
    torch.manual_seed(123)
    optimizer = torch.optim.AdamW(model.parameters(), lr=0.00005, weight_decay=0.1)
    num_epochs = 2
    train_losses, val_losses, tokens_seen = train_model_simple(
        model, train_loader, val_loader, optimizer, device,
        num_epochs=num_epochs, eval_freq=5, eval_iter=5,
        start_context=format_input(val_data[0]), tokenizer=tokenizer
    )
    end_time = time.time()
    execution_time_minutes = (end_time - start_time) / 60
    print(f"Training completed in {execution_time_minutes:.2f} minutes.")
    # generate 函数有个 max_new_tokens 参数（你代码里应该设了 35 或更大），它只在生成够指定长度才停，不会因为遇到 EOS 就提前终止。
    #
    # 所以模型输出 <|endoftext|> 后：
    #
    # 它觉得"上一段任务已结束"
    # 但还要凑够 token 数，于是它根据训练时见过的格式主动开了一个新对话