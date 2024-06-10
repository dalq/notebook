# 用迭代器替代while循环
import sys
f = open('sample.txt')
for c in iter(lambda: f.read(10), ''):
    n = sys.stdout.write(c)