# 分数的计算与处理
from fractions import Fraction
a = Fraction(3, 4)
b = Fraction(1, 4)
print(a + b)
print(a - b)
print(a * b)

# 将小数转化为分数
c = 3.75
d = Fraction(*c.as_integer_ratio())
print(d)