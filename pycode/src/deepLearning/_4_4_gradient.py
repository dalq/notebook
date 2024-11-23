import numpy as np
import matplotlib.pylab as plt


# 偏导数
def numerical_diff(f, x):
    h = 1e-4
    return (f(x + h) - f(x - h)) / (2 * h)


# 梯度
def numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x)  # 生成一个形状和x相同、所有元素都为0的数组

    for idx in range(x.size):
        tmp_val = x[idx]

        x[idx] = tmp_val + h
        f1 = f(x)

        x[idx] = tmp_val - h
        f2 = f(x)

        grad[idx] = (f1 - f2) / (2 * h)
        x[idx] = tmp_val
    return grad


# 梯度下降法, lr学习速率这种超参数，是需要人工设定的
def gradient_descent(f, int_x, lr=0.01, step_num=100):
    x = int_x  # 初始值

    for i in range(step_num):
        grad = numerical_gradient(f, x)
        x -= lr * grad  # 学习速率 * 梯度，去更新值

    return x


def function_1(x):
    return x ** 2 + 0.1 * x


def function_2(x):
    return x[0] ** 2 + x[1] ** 2


if __name__ == '__main__':
    # 求f1的偏导数
    print(numerical_diff(function_1, 5))
    # 求f2在某个点的梯度
    print(numerical_gradient(function_2, np.array([3.0, 4.0])))  # 输出numpy数组时，数值会被改写为易读的形式（取整）
    # 通过梯度下降法求f2的最小值
    print(gradient_descent(f=function_2, int_x=np.array([-3.0, 4.0]), lr=0.1, step_num=100))
