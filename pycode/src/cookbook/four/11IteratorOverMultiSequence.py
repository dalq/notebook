# 同时对多个序列进行迭代器操作
# zip()
from itertools import zip_longest

a = [1, 5, 4, 2, 10, 7]
b = [101, 78, 37, 15, 62, 99, 100, 100, 100, 100]

# 以最短的序列长度截止
for x, y in zip(a, b):
    print(x, y)

# 以最长的序列长度截止，可以添加fillvalue为填充元素
for i in zip_longest(a, b):
    print(i)

for i in zip_longest(a, b, fillvalue='X'):
    print(i)

# 应用：将俩数组构成一个kv字典
# s = dict(zip(a, b))
