from math import cos, sin, atan2, atan
from vector_drawing import *


# 极坐标转笛卡尔坐标
def to_cartesian(polar_vector):
    length_v, angle = polar_vector[0], polar_vector[1]
    return length_v * cos(angle), length_v * sin(angle)


# 计算向量的长度
def length(v):
    return sqrt(v[0] ** 2 + v[1] ** 2)


# 笛卡尔坐标转极坐标
def to_polar(vector):
    x, y = vector[0], vector[1]
    return length((x, y)), atan2(y, x)


def practice237():
    # 1000个极坐标对应的点
    polar_record = [(cos(5 * x * pi / 500.0), 2 * pi * x / 1000.0) for x in range(0, 1000)]
    # 极坐标点转为笛卡尔坐标
    vectors = [to_cartesian(p) for p in polar_record]
    # 用线段依次将其连接
    draw(Polygon(*vectors, color=blue), grid=None, axes=None, origin=None)


if __name__ == '__main__':
    # pi弧度 = 180度
    cartesian = to_cartesian((5, 37 * pi / 180))
    print(cartesian)
    print(to_polar((1, 0)))  # 0度
    print(to_polar((0, 1)))  # 90度

    print('cos(10π/6) = {}; sin(10π/6) = {}'.format(cos(10 * pi / 6), sin(10 * pi / 6)))
    # print('cos(10π/6) = ' + cos(10 * pi / 6) + ', sin(10π/6) = ' + sin(10 * pi / 6))
    practice237()  # 练习题2.37一朵五瓣花
    print('atan(-3/2)={}'.format(atan(-3/2) * 180 / pi))
