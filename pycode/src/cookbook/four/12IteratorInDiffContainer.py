# 在不同容器中迭代: itertools.chain()

from itertools import chain

a = [1, 2, 3, 4]
b = ['x', 'y', 'z']

# 比 x in a + b 性能好
for x in chain(a, b):
    print(x)