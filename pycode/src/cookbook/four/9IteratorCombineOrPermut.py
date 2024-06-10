# 迭代所有可能的组合或排列
from itertools import permutations, combinations

items = ['a', 'b', 'c']

for p in permutations(items):
    print(p)


# 两两组合的可能形式，无序
for c in combinations(items, 2):
    print(c)