# 将多个映射合并为单个映射
from collections import ChainMap
a = {
    'x': 1,
    'y': 2
}

b = {
    'm': 3,
    'n': 4
}

c = ChainMap(a, b)
# 并没有合并为一个字典，而只是简单维护一个底层映射关系的列表
# 如果有重复的key，使用第一个字典中的
# 用的是原始的字典，而不是new一个字典，如果a改了，chainMap也就改了。