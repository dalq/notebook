# 无穷大、 not a number
import math

a = float('inf')
print(a)
print(a + 45)

print(a / a)

c = float('nan')
d = float('nan')
print(c == d)
print(c is d)
print(math.isnan(c))