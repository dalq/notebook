import re
import importlib
import tiktoken

class SimpleTokenizerV1:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {index: token for token, index in vocab.items()}

    def encode(self, text):
        processed_text = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in processed_text if item.strip()]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids

    def decode(self, ids):
        # 每个str通过空格连接
        text = " ".join([self.int_to_str[i] for i in ids])
        # 移除标点符号前的空格
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
        return text

# 增加特殊次元
class SimpleTokenizerV2:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {index: token for token, index in vocab.items()}

    def encode(self, text):
        processed_text = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in processed_text if item.strip()]
        preprocessed = [item if item in self.str_to_int else '<|unk|>' for item in preprocessed]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids

    def decode(self, ids):
        # 每个str通过空格连接
        text = " ".join([self.int_to_str[i] for i in ids])
        # 移除标点符号前的空格
        text = re.sub(r'\s+([,.:;?!"()\'])', r'\1', text)
        return text


if __name__ == '__main__':
    with open("the-verdict.txt", "r", encoding="utf-8") as f:
        raw_text = f.read()
    processed_text = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
    preprocessed = [item.strip() for item in processed_text if item.strip()]

    # vocab构建
    all_words = sorted(set(preprocessed))
    vocab_size = len(all_words)  # 1130
    vocab = {token: index for index, token in enumerate(all_words)}

    # 封装好的tokenizer类
    tokenizer = SimpleTokenizerV1(vocab)
    ids = tokenizer.encode('Poor Money')
    print(ids)
    tokens = tokenizer.decode([80, 63])
    print(tokens)

    # 引入特殊次元（sorted之后都会返回列表）
    all_words.extend(["<|endoftext|>", "<|unk|>"])
    vocab = {token: index for index, token in enumerate(all_words)}
    vocab_items = list(vocab.items())
    print("vocab最后五个元素:", vocab_items[-5:])

    # 封装好的tokenizerV2类
    tokenizer = SimpleTokenizerV2(vocab)
    ids = tokenizer.encode('Heloo Poor Money')
    print(ids)
    tokens = tokenizer.decode([1131, 80, 63])
    print(tokens)

    # BytePair Encoding
    new_tokenizer = tiktoken.get_encoding("gpt2")
    text = """Hello, do you like tea? <|endoftext|> In the sunlit terraces
    of someunknownPlace."""
    integers = new_tokenizer.encode(text, allowed_special={"<|endoftext|>"})
    print(integers)
    strings = new_tokenizer.decode(integers)
    print(strings)
