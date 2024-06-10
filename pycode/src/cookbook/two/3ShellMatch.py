# 支持UNIX shell下的通配符模式
from fnmatch import fnmatch, fnmatchcase
print(fnmatch('123.txt', '*.txt'))

# 不忽略大小写
print(fnmatchcase('123.txt', '*.TXT'))
