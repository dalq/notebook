# 委托属性的访问
# 访问实例的属性时候，能够将其委托到一个内部持有的对象上


class A:
    def spam(self, x):
        pass


    def foo(self):
        pass


# 委托代替继承
# java中尽量用组合，而不要用继承类似
class B:
    def __init__(self):
        self._a = A()


    def bar(self):
        pass


    def __getattr__(self, name):
        # 最简单的形式可能是这样：
        # return self._a.spam(x)
        # return self._a.foo()
        # 但是这样需要些好几次，不如下面这样方便
        return getattr(self._a, name)