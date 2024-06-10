# 对迭代器做切片操作
import itertools

def count(n):
    while True:
        yield n
        n += 1


c = count(0)

# 切片类似于substring操作
for x in itertools.islice(c, 10, 20):
    print(x)