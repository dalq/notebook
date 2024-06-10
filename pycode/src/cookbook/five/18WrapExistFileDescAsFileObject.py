# 将已有的文件描述符包装为文件对象
import os

fd = os.open('samplefile.txt', os.O_RDONLY)

f = open(fd, 'rt')

for line in f:
    print(line)