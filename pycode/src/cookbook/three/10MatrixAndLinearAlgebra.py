# 矩阵运算以及线性代数
# matrix 相比于numpy.array来说 - 计算时候遵循线性代数规则
import numpy as np

m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
print(m)
# 转置
print(m.T)
# 逆矩阵
print(m.I)

# 更多线性代数操作
import numpy.linalg
print(numpy.linalg.det(m))
