import numpy as np

if __name__ == '__main__':
    x = np.array([[1.0, -0.5], [-2.0, 3.0]])
    print(x)
    mask = (x <= 0)
    print(mask)
    y = x.copy()
    y[mask] = 0
    print(y)
    print(x)

    # 验证广播机制
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[0, 100]])
    b1 = np.array([[0], [100]])
    b2 = np.array([[0, 100, 200]])  # 如果shape的和不一样，则广播会报错
    c = a + b
    c1 = a + b1
    c2 = a + b2
    print(f'a is: {a}, b is: {b}, c is: {c}, c1 is: {c1}, c2 is: {c2}')

