# 调用对象上的方法，方法名以字符串形式给出
# 其实就是类似于java中jmockit通过字符串形式Deencapsulation.invoke
# 也类似于HSF中执行泛华调用
import math, operator

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({!r:}, {!r:})'.format(self.x, self.y)

    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)

# 第一种方法
p = Point(2, 3)
d = getattr(p, 'distance')(0, 0)
print(d)

# 第二种方法
c = operator.methodcaller('distance', 0, 0)(p)
print(c)
