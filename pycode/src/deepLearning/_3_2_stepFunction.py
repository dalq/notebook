import numpy as np
import matplotlib.pyplot as plt


def step_function(x1):
    y = x1 > 0
    return y.astype(np.int_)


def step_function2(x2):
    return np.array(x2 > 0, dtype=np.int_)


def sigmoid(x3):
    return 1 / (1 + np.exp(-x3))


if __name__ == '__main__':
    x = np.array([-1.0, 1.0, 2.0])
    # 对NumPy数组进行不等号运算后，数组的各个元素都会进行不等号运算，生成一个布尔型数组。
    print(x > 0)
    print((x > 0).astype(np.int_))

    x = np.arange(-5.0, 5.0, 0.1)
    y = step_function(x)
    plt.plot(x, y)
    plt.ylim(-0.2, 1.2)
    plt.show()

    y2 = step_function2(x)
    plt.plot(x, y2, color='red')
    plt.ylim(-0.2, 1.2)
    plt.show()

    y3 = sigmoid(x)
    plt.plot(x, y3, color='green')
    plt.ylim(-0.2, 1.2)
    plt.show()
