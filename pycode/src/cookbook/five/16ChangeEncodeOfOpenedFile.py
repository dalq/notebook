# 为已经代开的文件添加或者修改编码方式
import sys
import io

print(sys.stdout.encoding)

print('Jalape\u00f1o')
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='ascii', errors='xmlcharrefreplace')
print('Jalape\u00f1o')