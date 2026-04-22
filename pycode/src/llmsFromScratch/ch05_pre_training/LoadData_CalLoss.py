import os
import time
import torch

from llmsFromScratch.ch02_data_process.SlideWindowSampling import create_dataloader_v1
from llmsFromScratch.ch04_gpt.YourGPTModel import GPTModel

GPT_CONFIG_124M = {
    "vocab_size": 50257,  # Vocabulary size
    "context_length": 256,  # 减小到1/4,减少了训练模型的计算需求，以便我们可以在标准笔记本电脑上进行训练
    "emb_dim": 768,  # Embedding dimension
    "n_heads": 12,  # Number of attention heads
    "n_layers": 12,  # Number of layers
    "drop_rate": 0.1,  # Dropout rate
    "qkv_bias": False  # Query-Key-Value bias
}

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ch02_data_process", "the-verdict.txt")
with open(file_path, "r", encoding="utf-8") as file:
    text_data = file.read()


train_ratio = 0.90 # 90%的数据进行训练，剩余的10%作为验证数据
split_idx = int(train_ratio * len(text_data))
train_data = text_data[:split_idx]
val_data = text_data[split_idx:]

train_loader = create_dataloader_v1(train_data, batch_size=2,
                                        max_length=GPT_CONFIG_124M["context_length"], stride=GPT_CONFIG_124M["context_length"], drop_last=True, shuffle=True, num_workers=0)

val_loader = create_dataloader_v1(val_data, batch_size=2,
                                        max_length=GPT_CONFIG_124M["context_length"], stride=GPT_CONFIG_124M["context_length"], drop_last=False, shuffle=False, num_workers=0)

def calc_loss_batch(input_batch, target_batch, model, device):
    input_batch, target_batch = input_batch.to(device), target_batch.to(device)
    logits = model(input_batch)
    loss = torch.nn.functional.cross_entropy(logits.flatten(0, 1), target_batch.flatten(0, 1))
    return loss

def calc_loss_loader(data_loader, model, device, num_batches = None):
    total_loss = 0.0
    if len(data_loader) == 0:
        return float("NaN")
    elif num_batches is None:
        num_batches = len(data_loader)
    else:
        num_batches = min(num_batches, len(data_loader))

    for i, (input_batch, target_batch) in enumerate(data_loader):
        if i >= num_batches:
            break
        loss = calc_loss_batch(input_batch, target_batch, model, device)
        total_loss += loss.item()
    return total_loss / num_batches

if __name__ == '__main__':
    print("Train loader:") # 9个训练集批次
    for x, y in train_loader:
        print(x.shape, y.shape)

    print("\nValidation loader:") # 1个验证集批次
    for x, y in val_loader:
        print(x.shape, y.shape)

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

    print(f"Using {device} device.")

    model = GPTModel(GPT_CONFIG_124M)
    model.eval()
    model.to(device)
    torch.manual_seed(123)

    start_time = time.time()
    with torch.no_grad():  # Disable gradient tracking for efficiency because we are not training, yet
        train_loss = calc_loss_loader(train_loader, model, device)
        print(f"[{time.time() - start_time:.2f}s] Training loss: {train_loss}")
        val_loss = calc_loss_loader(val_loader, model, device)
        print(f"[{time.time() - start_time:.2f}s] Validation loss: {val_loss}")

    print(f"[{time.time() - start_time:.2f}s] Total evaluation done.")