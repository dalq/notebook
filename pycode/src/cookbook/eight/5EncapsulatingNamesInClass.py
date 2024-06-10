# 将名称封装到类中
# python中，竟然是通过特定的命名规则来表达对数据和方法的用途


class A:
    def __init__(self):
        self._internal = 0 # 约定这样为私有属性
        self.public = 1    # 预定这样为共有属性

    def public_method(self):
        '''
        公有方法
        '''

    def _internal_method(self):
        '''
        私有方法
        '''

    # 双下划线的名称 -> 会被重命名为_A__private
    # 如果B继承A，-> 他的方法不会被覆盖，而是会被重命名为_B__private
    def __private(self):
        self.__private = 0