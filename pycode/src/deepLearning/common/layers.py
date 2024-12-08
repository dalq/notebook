import numpy as np
from functions import softmax, cross_entropy_error


class Relu:
    def __init__(self):
        self.mask = None

    def forward(self, x):
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0
        return out

    def backward(self, dout):
        dout[self.mask] = 0  # mask中为true的index，dout设置为0
        dx = dout
        return dx


class Sigmoid:
    def __init__(self):
        self.out = None

    def forward(self, x):
        out = 1 / (1 + np.exp(-x))
        self.out = out
        return out

    def backward(self, dout):
        dx = dout * self.out * (1 - self.out)  # dout * y * (1-y)
        return dx


class Affine:
    def __init__(self, W, b):
        self.W = W
        self.b = b
        self.x = None
        self.dW = None
        self.db = None

    def forward(self, x):
        self.x = x
        out = np.dot(x, self.W) + self.b
        return out

    def backward(self, dout):
        dx = np.dot(dout, self.W.T)
        self.dW = np.dot(self.x.T, dout)
        # 因为这个参数B在正向传播是会作用于每一行，所以其实它稍微变化一下，对每一行的结果都有影响。
        # 那么反过来，已知了每一行对最终损失函数的影响以后，需要把他们都加起来，才是这个偏置变量B对损失函数最终的影响
        self.db = np.sum(dout, axis=0)
        return dx


class SoftmaxWithLoss:
    def __init__(self):
        self.loss = None
        self.y = None
        self.t = None

    def forward(self, x, t):
        self.t = t
        self.y = softmax(x)
        self.loss = cross_entropy_error(self.y, self.t)
        return self.loss

    # 使用交叉熵误差作为softmax函数的损失函数后，反向传播得到(y1-t1, y2-t2, y3-t3)￼这样“漂亮”的结果
    # 或者说，为了得到这样的结果，特意设计了交叉熵误差函数。
    def backward(self, dout=1):
        batch_size = self.t.shape[0]
        dx = (self.y - self.t) / batch_size
        return dx
