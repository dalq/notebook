# 将二进制数据读取到可变缓冲区中
import os.path


def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        # 把已经定义好的缓冲区填满，可以避免产生额外的内存分配动作
        f.readinto(buf)
    return buf

bb = read_into_buffer('samplefile.txt')
print(bb[0:3])