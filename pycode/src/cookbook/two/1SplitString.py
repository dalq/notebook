# 针对任意多的分隔符拆分字符串
# 简单的使用split()
# 复杂的使用re.split()

import re

line = 'asdfs sldfsf; sdfsa, sdfsadf, sdf,      foo'
# 分隔符为分号、逗号，或者空格符；他们都免可以有任意多的空格符
regex_line = re.split(r'[;,\s]\s*', line)
print(regex_line)

a = ['a', 'b', 'c', 'd']
b = ['@', '#', '$', '%']
print(''.join(v + d for v, d in zip(a, b)))