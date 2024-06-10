# 对其文本字符串
# ljust、rjust、center
# 或者format
text = 'hello world'
a1 = text.ljust(20, '=')
a2 = text.rjust(20, '=')
a3 = text.center(20, '=')

print(a1)
print(a2)
print(a3)

# 指定空格以外的字符，需要在<>^之前增加
b1 = format(text, '=>20')
b2 = format(text, '*<20')
b3 = format(text, '#^20')
print(b1)
print(b2)
print(b3)

# format的其他用法
# todo 这里不能增加空格意外的字符吗
c = '{:>10s} {:>10s}'.format('Hello', 'World')
print(c)
print(format(1.23456, '^10.2f'))
