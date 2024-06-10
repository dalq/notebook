# 在子类中扩展属性

class Person:
    def __init__(self, name):
        self.name = name

    # getter
    @property
    def name(self):
        return self._name

    # setter
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            # 应该和java中的throws作用一样
            raise TypeError('Expected a string')
        self._name = value

    # delete
    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")


class SubPerson(Person):
    @Person.name.getter
    def name(self):
        print('Getting name')
        return super().name

p = Person('dalq')
print(p.name)

s = SubPerson('new dalq')
print(s.name)