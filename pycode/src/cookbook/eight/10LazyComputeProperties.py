# 让属性具有惰性求值的能力
# 只有访问这个属性时候才参与计算，但是一旦访问了改属性，希望把计算出的值缓存起来
import math

class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('computing area')
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('computing perimeter')
        return 2 * math.pi * self.radius


c = Circle(4.0)
print(c.radius)
print(c.area)
print(c.perimeter)
print(c.area)
print(c.perimeter)
# 但是要注意到c.area是可变的