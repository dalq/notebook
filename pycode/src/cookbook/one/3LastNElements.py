# deque双端队列，先进先出
# 也支持popLeft、appendLeft
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            # 生成器函数？
            yield line, previous_lines
        previous_lines.append(line)


lines = ['test1', 'test2', 'test3python', 'test4python', 'test5python', 'test6python', 'test7python']


for line, prevlines in search(lines, 'python', 5):
    for pline in prevlines:
        print(pline, end='^_^')
    print(line, end='@_@')
    print('-'*20)
print(prevlines)
