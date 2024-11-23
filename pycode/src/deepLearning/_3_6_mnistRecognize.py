from mnist import load_mnist
import numpy as np
from PIL import Image
import pickle
from common.functions import sigmoid, softmax


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()


def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test


def init_network():
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    return network


def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y


if __name__ == '__main__':
    # 读取数据
    (x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)
    print(x_train.shape)
    print(t_train.shape)
    print(x_test.shape)
    print(t_test.shape)

    # 读取并画出第一个数据“5”
    img = x_train[0]
    label = t_train[0]
    print(label)
    print(img.shape)
    img = img.reshape(28, 28)
    print(img.shape)
    img_show(img)

    # 评价神经网络推理的精度
    x, t = get_data()
    network = init_network()
    accuracy_cnt = 0
    for i in range(len(x)):
        y = predict(network, x[i])
        p = np.argmax(y)  # 获取最大值的索引
        if p == t[i]:
            accuracy_cnt += 1
    print("Accuracy: " + str(accuracy_cnt / len(x)))

    tmp = x[0] * 255  # 由于读取的时候做了归一化，如果要还原图像需要再乘回去255
    tmp = tmp.reshape(28, 28)
    img_show(tmp)

    # 评价神经网络推理的精度 -- 批处理版本
    x, t = get_data()
    network = init_network()
    batch_size = 100
    accuracy_cnt = 0
    for i in range(0, len(x), batch_size):  # 修改点1
        y_batch = predict(network, x[i: i + batch_size])  # 修改点2
        p = np.argmax(y_batch, axis=1)  # 修改点3
        #  print(p == t[i: i + batch_size]) 返回boolean数组
        accuracy_cnt += np.sum(p == t[i: i + batch_size])  # 修改点4
    print("[batch] Accuracy: " + str(accuracy_cnt / len(x)))
