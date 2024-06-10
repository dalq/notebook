# 文本模式的匹配和查找
import re
text1 = '09/08/2018'
text2 = 'Sep 8, 2018'

# 数字通配符需要转义：\d
# todo r模式
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

pattern = re.compile(r'\d+/\d+/\d+')
# print(pattern.match(text1))这样不行！
if pattern.match(text1):
    print('Y')
else:
    print('N')

# find all 方法实例
text3 = 'Today is 09/08/2018, tomorrow is 09/10/2018'
print(pattern.findall(text3))

# 提取匹配的分组
pattern2 = re.compile(r'(\d+)/(\d+)/(\d+)')
m = pattern2.match('09/08/2018')
print(m.group(0), ' --- ', m.group(1), ' --- ', m.group(2), ' --- ', m.groups())

for month, day, year in pattern2.findall(text3):
    print('{}-{}-{}'.format(year, month, day))