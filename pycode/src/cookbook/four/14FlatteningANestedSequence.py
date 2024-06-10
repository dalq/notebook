# 展开处理 嵌套型 的序列？
# yield from命令：将嵌套类型的拍平
from collections import Iterable


# str迭代会成为char
def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x


items = [1, 2, [3, 4, [5, 6], 7], 8]
for y in flatten(items):
    print(y)