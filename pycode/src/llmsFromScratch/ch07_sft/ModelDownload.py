import torch
import tiktoken
from gpt_download import download_and_load_gpt2
from llmsFromScratch.ch04_gpt.YourGPTModel import GPTModel
from llmsFromScratch.ch05_pre_training.WeightsDownload import load_weights_into_gpt, generate
from llmsFromScratch.ch05_pre_training.EvaluateTextModel import text_to_token_ids, token_ids_to_text
from llmsFromScratch.ch07_sft.DataSetPrepare import format_input, download_and_load_file

BASE_CONFIG = {
    "vocab_size": 50257,     # 词汇表大小
    "context_length": 1024,  # 上下文长度
    "drop_rate": 0.0,        # dropout率
    "qkv_bias": True         # Query-key-value 偏置
}

model_configs = {
    "gpt2-small (124M)": {"emb_dim": 768, "n_layers": 12, "n_heads": 12},
    "gpt2-medium (355M)": {"emb_dim": 1024, "n_layers": 24, "n_heads": 16},
    "gpt2-large (774M)": {"emb_dim": 1280, "n_layers": 36, "n_heads": 20},
    "gpt2-xl (1558M)": {"emb_dim": 1600, "n_layers": 48, "n_heads": 25},
}

CHOOSE_MODEL = "gpt2-medium (355M)"


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

    # 使用验证集中第一个样本进行评估
    ## 数据load
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
    val_data = data[train_portion + test_portion:]

    # 用第一个样本数据对GPT进行验证
    torch.manual_seed(123)
    input_text = format_input(val_data[0])
    print(input_text)

    tokenizer = tiktoken.get_encoding("gpt2")
    # generate是generate_text_simple的升级版,增加了temperature和 top-k
    token_ids = generate(
        model=model,
        idx=text_to_token_ids(input_text, tokenizer),
        max_new_tokens=35,
        context_size=BASE_CONFIG["context_length"],
        eos_id=50256,
    )
    generated_text = token_ids_to_text(token_ids, tokenizer)
    # generate函数返回的是拼接在一起的输入和输出文本,我们这里仅关注模型生成的回复
    response_text = (
        generated_text[len(input_text):]
        .replace("### Response:", "")
        .strip()
    )
    print("\n\nsft前的基线表现====")
    print(response_text)

