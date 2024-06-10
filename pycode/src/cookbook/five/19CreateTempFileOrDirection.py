# 创建临时文件和目录
from tempfile import TemporaryFile, TemporaryDirectory

with TemporaryFile('w+t') as f:
    f.write('hello world\n')
    f.write('test\n')
    f.seek(0)
    data = f.read()
    print(data)

import tempfile

print(tempfile.mkstemp())