# 创建可管理的属性

class Person:
    def __init__(self, first_name):
        self.first_name = first_name


    #Getter
    # 只有定义了property才能使用setter和deleter
    @property
    def first_name(self):
        return self._first_name


    #Setter
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Excepted a string')
        self._first_name = value


    # detele
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")


# use getter
a = Person('dalq')
print(a.first_name)

a.first_name = 42

# 实际中我们更希望采用bean的形式，直接显示地采用set/get方法会比通过property隐式调用更贱方便和简单
# p = Person('name')
# p.get_first_name()
# p.set_first_name('new')