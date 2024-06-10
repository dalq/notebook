# 修改实例的字符串表示


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # !r 不显示Pair(3, 4) 只显示(3, 4)
    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)
    def __str__(self):
        # 参数0的x属性
        return '({0.x!s}, {0.y!s})'.format(self)


p = Pair(3, 4)
## __repr__:
p
## __str__:
print(p)