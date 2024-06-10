# 创建一种新形式的类属性或实例属性

class Integer:
    def __init__(self, name):
        self.name = name


    def __get__(self, instance, cls):
        if isinstance is None:
            return self
        else:
            return instance.__dict__[self.name]


    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value


class Point:
    x = Integer('x')
    y = Integer('y')
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(2, 3)
print(p.x)
print(p.y)

p.x = 3
print(p.x)
print(p.y)

p.x = 2.1