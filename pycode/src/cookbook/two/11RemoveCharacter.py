# 从字符串中去掉不需要的字符
# 只会对两边的起效果，中间的不管用的！
# 可以使用replace
s = '  hello world \n'
print(s)
print(s.strip())
print(s.lstrip())
print(s.rstrip())