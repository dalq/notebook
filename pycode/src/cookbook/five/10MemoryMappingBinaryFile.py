# 对二进制文件做内存映射
import os
import mmap
from datetime import datetime

# ACCESS_WRITE：会写回原文件
# ACCESS_COPY：指向在本地修改数据，并不想将这些修改写回原始文件中
# ACCESS_READ：只读访问


def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)


m = memory_map('mmap.txt')
now = datetime.today().strftime("%Y-%m-%d %H:%M")
m[13:29] = bytes(now, encoding='utf-8')
print(m[0])
m[0] = 117
m.close()
# why not change the file?