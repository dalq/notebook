# 读写压缩的数据文件
# gzip或者bz2

import gzip
with gzip.open('testzip.gzip', 'wt') as f:
    f.write('123321')

with gzip.open('testzip.gzip', 'rt') as f:
    text = f.read()
print(text)