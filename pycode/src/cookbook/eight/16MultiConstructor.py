# 在类中定义多个构造函数
import time

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # -
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)

    def __str__(self):
        return '{} - {} - {}'.format(self.year, self.month, self.day)


a = Date(2019, 2, 16)
print(a)
b = Date.today()
print(b)