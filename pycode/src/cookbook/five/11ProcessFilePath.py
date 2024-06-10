# 处理路径名
import os

path = 'samplefile.txt'

print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.splitext(path))