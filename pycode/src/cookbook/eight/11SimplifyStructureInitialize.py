# 简化数据结构的初始化过程
# 将初始化数据结构的步骤归纳到单独的一个__init__()函数中
# 并将其定义在一个公共的基类中
import math

class Structure:
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        #set
        for name, value in zip(self._fields, args):
            setattr(self, name, value)


# example
if __name__ == '__main__':
    class Stock(Structure):
        _fields = ['name', 'shares', 'price']
    class Point(Structure):
        _fields = ['x', 'y']
    class Circles(Structure):
        _fields = ['radius']
        def area(self):
            return math.pi * self.radius ** 2

s = Stock('ACME', 50, 91.1)
p = Point(2, 3)
c = Circles(4.5)
c = Circles(4,5, 1)