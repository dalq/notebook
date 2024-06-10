# 当创建大量实例时如何节省内存
# __slot__属性


class Date:
    __slots__ = ['year', 'month', 'day']

    # 类似于class 的static变量？
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

