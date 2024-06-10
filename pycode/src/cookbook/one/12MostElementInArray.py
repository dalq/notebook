# 找到出现次数最多的元素
# 由于返回的是map，所以可以对于返回的字典做集合操作(+-)
from collections import Counter


words = ['a', 'b', 'c', 'd', 'c', 'a', 'c', 'd', 'f']
words_count = Counter(words)
print(words_count)

top_three = words_count.most_common(3)
print(top_three)