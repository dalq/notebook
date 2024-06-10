# 处理大型数组 - NumPy库
# pip3 install numpy 来安装
import numpy as np
x = [1, 2, 3, 4]
print(x * 2)
#print(x + 10)

y = np.array([1, 2, 3, 4])
# numpy针对标量运算时是针对逐个元素进行计算的
print(y * 2)
print(y + 10)

# 矩阵运算非常方便
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
print(a[1])
print(a[:, 1])