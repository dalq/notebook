# 在字符串上执行I/O操作
# 模拟一个文件
# 在内存中以 io 流的方式读写 str

from io import StringIO

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')

print(f.getvalue())