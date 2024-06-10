# 读写二进制个结构的数组

# 将元组写入到二进制文件中，通过struct模块将每个元组编码为一个结构
from struct import Struct


def write_records(records, format, f):
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))


ex_records = [(1, 2.3, 4.5), (6, 7.8, 9.0), (12, 13.4, 567)]

with open('res/binaryArray.b', 'wb') as f:
    write_records(ex_records, '<idd', f)


# 读取文件，解析为元组
    ## 方法一：增量方式读取文件
def read_records(format, f):
    record_struct = Struct(format)
    chunks = iter(lambda : f.read(record_struct.size), b'')
    return (record_struct.unpack(chunk) for chunk in chunks)


with open('res/binaryArray.b', 'rb') as f:
    for rec in read_records('<idd', f):
        print(rec)

    ## 方法二：全部一次性读取
def unpack_records(format, data):
    record_struct = Struct(format)
    return (record_struct.unpack_from(data, offset) for offset in range(0, len(data), record_struct.size))


with open('res/binaryArray.b', 'rb') as f:
    data = f.read()

for rec in unpack_records('<idd', data):
    print(rec)


# 当然更推荐使用numpy函数
import numpy as np
f = open('res/binaryArray.b', 'rb')
records = np.fromfile(f, dtype='<i,<d,<d')
print(records)