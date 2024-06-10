# 将字符串转换为日期
from datetime import datetime

text = '2018-10-21'
y = datetime.strptime(text, '%Y-%m-%d')
print(y)

z = datetime.strftime(y, '%A, %B, %d, %Y')
print(z)