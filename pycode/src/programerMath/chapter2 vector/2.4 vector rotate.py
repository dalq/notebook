from math import cos, sin, atan2
from vector_drawing import *


# 计算向量的长度
def length(v):
    return sqrt(v[0] ** 2 + v[1] ** 2)


# 笛卡尔坐标转极坐标
def to_polar(vector):
    x, y = vector[0], vector[1]
    return length((x, y)), atan2(y, x)


# 极坐标转笛卡尔坐标
def to_cartesian(polar_vector):
    length_v, angle = polar_vector[0], polar_vector[1]
    return length_v * cos(angle), length_v * sin(angle)


# 将向量旋转指定的角度
def rotate(angle, vectors):
    polar_vector = [to_polar(v) for v in vectors]
    rotate_polar_vector = [(l, a + angle) for (l, a) in polar_vector]
    return [to_cartesian(rp) for rp in rotate_polar_vector]


def add(v1, v2):
    return v1[0] + v2[0], v1[1] + v2[1]


# 平移向量
def translate(translation, vectors):
    return [add(translation, v) for v in vectors]


# 返回n边形
def regular_polygon(n):
    return [to_cartesian((7, 2 * pi * k / n)) for k in range(0, n)]


if __name__ == '__main__':
    dino_vectors = [(6, 4), (3, 1), (1, 2), (-1, 5), (-2, 5), (-3, 4), (-4, 4),
                    (-5, 3), (-5, 2), (-2, 2), (-5, 1), (-4, 0), (-2, 1), (-1, 0), (0, -3),
                    (-1, -4), (1, -4), (2, -3), (1, -2), (3, -1), (5, 1)
                    ]
    rotate_dinos = rotate(pi / 4, dino_vectors)
    rotate_translate_dinos = translate((8, 8), rotate(5 * pi / 3, dino_vectors))
    translate_rotate_dinos = rotate(5 * pi / 3, translate((8, 8), dino_vectors))
    regula_8 = regular_polygon(8)
    draw(
        # Points(*dino_vectors, color=red),
        # Points(*rotate_dino_vectors, color=blue)
        Polygon(*dino_vectors, color=red),
        Polygon(*rotate_dinos, color=blue),
        Polygon(*rotate_translate_dinos, color=green),
        Polygon(*translate_rotate_dinos, color=purple),
        Polygon(*regula_8, color=gray),
    )
