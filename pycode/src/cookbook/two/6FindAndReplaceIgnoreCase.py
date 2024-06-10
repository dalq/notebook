# 以不区分大小写的方式对文本做查找和替换
import re

text = 'UHUND, PYTHON, python, asdf'
f = re.findall('python', text, flags=re.IGNORECASE)
print(f)

# 复杂的替换，使用re模块的sub函数
# 简单的可以使用str的replace
f1 = re.sub('python', 'java', text, flags=re.IGNORECASE)
print(f1)
# todo sub不会按照原来的大小写规则，这里显示的都是小写