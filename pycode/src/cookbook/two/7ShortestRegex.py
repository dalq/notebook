# 避免贪婪模式(找出最长的可能匹配)
import re

text = 'Commputer says "no." Phone says "yes." '
patten = re.compile(r'\"(.*)\"')
result = patten.findall(text)
print(result)
# 他会把最长的""区间匹配出来

# 问题解决：*后面加上？
patten2 = re.compile(r'\"(.*?)\"')
result = patten2.findall(text)
print(result)

# 总结，在*或者+后面添加一个?，会强制把匹配算法调整为寻找最短的可能匹配
