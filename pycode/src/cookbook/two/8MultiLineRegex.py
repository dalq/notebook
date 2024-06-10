# 如何匹配多行的情况
# 一种是添加非捕获组
# 一种是添加re.DOTALL，可以让正则表达式中的.能够匹配所有的字符，也包括换行符
import re
text = '''/* this is a
        multiline comment */'
'''
print(text)

pattern = re.compile(r'/\*(.*?)\*/')
result = pattern.findall(text)
print(result)

# use (?:/|\n)指定一个非捕获组，只做匹配但是不补货结果，也不会分配组号
# 把.替换为上述
pattern2 = re.compile(r'/\*((?:.|\n)*?)\*/')
result = pattern2.findall(text)
print(result)

# usere.DOTALL
pattern3 = re.compile(r'/\*(.*?)\*/', re.DOTALL)
result = pattern3.findall(text)
print(result)