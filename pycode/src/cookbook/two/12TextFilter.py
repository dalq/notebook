# 文本过滤与清理
# str.translate()
import unicodedata
import sys

s = 'pýtĥöñ\fis\tawesome\r\n'
print('s= ' + s)

# step 1. 清理空格：将\t \n这种，重新映射为单独的空格，回车\r直接删除(映射为None)
remap = {
    # todo ? what's this
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None
}
a = s.translate(remap)
print('a= ' +a)

# step 2. 清理掉所有的unicode组合字符
# 构建，将每一个unicode组合字符都映射为None的字典
cbm_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD', a)
print('b= ' +b)
bb = b.translate(cbm_chrs)
print('b= ' +bb)

# 关于组合字符
print('n 和 ' + '\u0303' + ' 组合在一起竟然是：' + 'n\u0303')
