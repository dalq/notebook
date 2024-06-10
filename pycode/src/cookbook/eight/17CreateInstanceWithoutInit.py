# 不通过调用init来创建实例
# __new__()创建一个位初始化的实例


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


d = Date.__new__(Date)
# 会报错
# print(d.year)

date = {'year': 2019, 'month': 2, 'day': 17}
for key, value in date.items():
    # see 11SimplifyStructureInitialize.py
    setattr(d, key, value)
# 不会报错了
print(d.year)