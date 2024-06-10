# 精确的小数计算，decimal模块
from decimal import Decimal
a = 4.2
b = 2.1
c = a + b
print(c)

a = Decimal('4.2')
b = Decimal('2.1')
c = a + b
print(c)