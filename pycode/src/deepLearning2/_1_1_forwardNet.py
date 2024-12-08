import numpy as np


class Sigmoid:
    def __init__(self):
        self.params = []

    def forward(self, x):
        return 1 / (1 + np.exp(-x))


class Affine:
    def __init__(self, W, b):
        self.params = [W, b]

    def forward(self, x):
        W, b = self.params
        out = np.dot(x, W) + b
        return out


class TwoLayerNet:
    def __init__(self, input_size, hidden_size, output_size):
        W1 = np.random.randn(input_size, hidden_size)
        b1 = np.random.randn(hidden_size)
        W2 = np.random.randn(hidden_size, output_size)
        b2 = np.random.randn(output_size)

        # 3层神经网络
        self.layers = [
            Affine(W1, b1),
            Sigmoid(),
            Affine(W2, b2)
        ]

        # 没看懂，貌似下面也用不到，应该是为了后面推理方便拿出来参数
        self.params = []
        for layer in self.layers:
            self.params += layer.params

    def predict(self, x):
        for layer in self.layers:
            x = layer.forward(x)
        return x


if __name__ == '__main__':
    a = np.array([1, 2, 3])
    b = np.array([[1], [2], [3]])
    print(a.shape)
    print(b.shape)
    x = np.random.randn(10, 2)
    model = TwoLayerNet(2, 4, 3)
    y = model.predict(x)
    print(y)
