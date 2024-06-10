# 将unicode文本统一标示为规范形式
# Unicode展示不一致，可能是\u00f1o，可能是\u0303o
# todo 一种是真正的个体字符（一个）；一种是n+~，组合而成的字符(二个)
# 他们俩的字节码不一样的！展示确是一样的！
import unicodedata


s1 = 'this is \u00f1'
s2 = 'this is n\u0303'
print(s1)
print(s2)

# 解决办法
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print('字符是{} ascii是{}'.format(t1, ascii(t1)))
print('字符是{} ascii是{}'.format(t2, ascii(t2)))

t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
print('字符是{} ascii是{}'.format(t3, ascii(t3)))
print('字符是{} ascii是{}'.format(t4, ascii(t4)))