# 对固定大小的记录进行迭代
from functools import partial

RECORE_SIZE = 2

with open('samplefile.txt', 'rb') as f:
    records = iter(partial(f.read, RECORE_SIZE), b'')
    for r in records:
        print(r, sep='*', end='#')