# OrderedDic，java中应该是TreeMap
# 遍历时，会严格按照初始添加的顺序进行

from collections import OrderedDict
d = OrderedDict()
d['foo'] = 1
d['foo2'] = 2
d['foo4'] = 4
d['foo3'] = 3

for key in d:
    print(key, d[key])

# 低层是双向链表
# java中的TreeMap低层是红黑树
