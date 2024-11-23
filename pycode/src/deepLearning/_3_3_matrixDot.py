import numpy as np

if __name__ == '__main__':
    A = np.array([[1, 2], [3, 4], [5, 6]])
    B = np.array([7, 8])  # 列，竖的
    print(A.shape)
    print(B.shape)
    C = np.dot(A, B)
    print(C)
    print(C.shape)
