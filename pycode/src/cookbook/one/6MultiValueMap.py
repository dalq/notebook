# 字典中讲键映射到多个值上
# 思路，讲value设置为集合(List、Set)
# 如果希望消除重复元素 - Set
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
print(d.get('a'))

# 如果不希望在初始化时自动创建字典表项，可以使用setdefault
# 我的理解应该是先不new出这个对象