# 定义带有额外状态的生成器函数
# 生成器逻辑放到__iter__()中
from collections import deque


class linehistory:
    def __init__(self, lines, hislen=3):
        self.lines = lines
        self.history = deque(maxlen=hislen)

    def __iter__(self):
        # 参考4.10：以索引-值对的心事迭代序列
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(selfself):
        selfself.history.clear()


with open('sample.txt') as f:
    lines = linehistory(f)
    for line in lines:
        if 'python' in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='')