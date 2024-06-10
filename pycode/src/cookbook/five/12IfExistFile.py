# 检测文件是否存在
import os
import time

print(os.path.exists('simplefile.txt'))

print(os.path.exists('/etc/hosts'))

# 是否是文件
# 是否是路径
print(os.path.isdir('/usr/bin'))

# 获取文件属性
print(os.path.getmtime('/etc/hosts'))
print(time.ctime(os.path.getmtime('/etc/hosts')))
print(os.path.getsize('/etc/hosts'))