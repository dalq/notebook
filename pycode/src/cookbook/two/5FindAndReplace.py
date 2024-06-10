# 简单的替换使用replace
# 复杂的使用re模块的sub()函数
import re
from calendar import month_abbr
text3 = 'Today is 09/08/2018, tomorrow is 09/10/2018'
result = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text3)
print(result)


# 更加复杂的(比如要格式化输出)，使用回调函数
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))


pattern = re.compile(r'(\d+)/(\d+)/(\d+)')
result2 = pattern.sub(change_date, text3)
print(result2)