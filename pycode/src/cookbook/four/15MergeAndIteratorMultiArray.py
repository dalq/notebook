# 合并多个有序队列，然后对结果进行迭代
import heapq

a = [1, 3, 5, 7]
b = [2, 4, 6, 8]

# 可迭代特性意味着它不会立马读取所有序列
# 需要所有输入序列必须是排过序的
for c in heapq.merge(a, b):
    print(c)
