import numpy as np
from common.functions import softmax, cross_entropy_error
# from _4_4_gradient import gradient_descent, numerical_gradient
from common.gradient import numerical_gradient


class SimpleNet:
    def __init__(self):
        self.W = np.random.randn(2, 3)

    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)
        return loss


if __name__ == '__main__':
    net = SimpleNet()
    x = np.array([0.6, 0.9])
    t = np.array([0, 0, 1])
    p = net.predict(x)

    print(net.W)
    print(p)
    print(np.argmax(p))
    print(net.loss(x, t))

    f = lambda w: net.loss(x, t)
    dW = numerical_gradient(f, net.W)
    print(dW)
