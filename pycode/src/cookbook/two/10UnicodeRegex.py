# 使用正则表达式处理unicode字符
import re


pattern = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]]+')
text = "hello world"
result = pattern.findall(text)
print(result)

text2 = 'العربية'
print(ascii(text2))
result = pattern.findall(text2)
# todo 为什么没有匹配出来呢？
print(result)