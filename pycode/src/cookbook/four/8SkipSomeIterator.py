# 跳过可迭代对象中的前一部分元素
# itertools中的dropwhile函数
from itertools import dropwhile
with open('sample.txt') as f:
    for line in dropwhile(lambda line : line.startswith('1'), f):
        print(line, end='')
        #todo 只有第一行好使，why？