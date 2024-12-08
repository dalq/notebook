# 2层神经网络解决螺旋数据分类问题
import numpy as np
import matplotlib.pyplot as plt
from dataset import spiral
from common.layers import Affine, Sigmoid, SoftmaxWithLoss
from common.optimizer import SGD


class TwoLayerNet:
    def __init__(self, input_size, hidden_size, output_size):
        I, H, O = input_size, hidden_size, output_size

        W1 = 0.01 * np.random.randn(I, H)
        b1 = np.zeros(H)
        W2 = 0.01 * np.random.randn(H, O)
        b2 = np.zeros(O)

        self.layers = [
            Affine(W1, b1),
            Sigmoid(),
            Affine(W2, b2)
        ]
        self.loss_layer = SoftmaxWithLoss()
        self.params, self.grads = [], []
        for layer in self.layers:
            self.params += layer.params
            self.grads += layer.grads

    def predict(self, x):
        for layer in self.layers:
            x = layer.forward(x)
        return x

    def forward(self, x, t):
        score = self.predict(x)
        loss = self.loss_layer.forward(score, t)
        return loss

    def backward(self, dout=1):
        dout = self.loss_layer.backward(dout)
        for layer in reversed(self.layers):
            dout = layer.backward(dout)
        return dout


if __name__ == '__main__':
    x, t = spiral.load_data()
    print('x', x.shape)  # (300, 2)
    print('t', t.shape)  # (300, 3)

    # 画出数据集
    N = 100
    CLS_NUM = 3
    markers = ['o', 'x', '^']
    for i in range(CLS_NUM):
        plt.scatter(x[i * N:(i + 1) * N, 0], x[i * N:(i + 1) * N, 1], s=40, marker=markers[i])
    plt.show()

    # 通过神经网络学习数据集
    # 1、超参数
    max_epoch = 300
    batch_size = 30
    hidden_size = 10
    learning_rate = 1.0
    # 2、对读入的数据，生成模型和 优化器？
    # x, t = spiral.load_data()
    model = TwoLayerNet(input_size=2, hidden_size=hidden_size, output_size=3)
    optimizer = SGD(lr=learning_rate)
    #
    data_size = len(x)
    max_iters = data_size
    total_loss = 0
    loss_count = 0
    loss_list = []

    for epoch in range(max_epoch):
        # 3、打乱数据
        idx = np.random.permutation(data_size)
        x = x[idx]
        t = t[idx]

        for iters in range(max_iters):
            batch_x = x[iters * batch_size: (iters + 1) * batch_size]
            batch_t = t[iters * batch_size: (iters + 1) * batch_size]
            # 4、计算梯度更新参数
            loss = model.forward(batch_x, batch_t)
            model.backward()
            optimizer.update(model.params, model.grads)

            total_loss += loss
            loss_count += 1
            # 5、定期输出学习过程
            if (iters + 1) % 10 == 0:
                avg_loss = total_loss / loss_count
                print('| epoch %d |  iter %d / %d | loss %.2f'
                      % (epoch + 1, iters + 1, max_iters, avg_loss))
                loss_list.append(avg_loss)
                total_loss, loss_count = 0, 0

    plt.plot(np.arange(len(loss_list)), loss_list, label='train')
    plt.xlabel('iterations (x10)')
    plt.ylabel('loss')
    plt.show()
