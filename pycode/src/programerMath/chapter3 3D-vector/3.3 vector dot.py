from math import sqrt, acos, pi, cos, sin
from random import random


def dot(u, v):
    return sum([coord1 * coord2 for coord1, coord2 in zip(u, v)])


def scale(scalar, v):
    return tuple(scalar * coord for coord in v)


def length(v):
    return sqrt(sum([coord ** 2 for coord in v]))


# 🔥计算两个向量的夹角
def angle_between(v1, v2):
    return acos(dot(v1, v2) / (length(v1) * length(v2)))


# 极坐标转笛卡尔坐标
def to_cartesian(polar_vector):
    length_v, angle = polar_vector[0], polar_vector[1]
    return length_v * cos(angle), length_v * sin(angle)


def random_vector_of_length(l):
    return to_cartesian((l, 2 * pi * random()))


if __name__ == '__main__':
    print('dot((1, 0), (0, 2)) = {}'.format(dot((1, 0), (0, 2))))
    print('dot((3, 4), (2, 3)) = {}'.format(dot((3, 4), (2, 3))))
    print('dot((6, 8), (2, 3)) = {}'.format(dot(scale(2, (3, 4)), (2, 3))))
    print('dot((3, 4), (4, 6)) = {}'.format(dot((3, 4), scale(2, (2, 3)))))

    tmp = angle_between((1, 0), (0, 1))
    print('angle_between((1, 0), (0, 1)) = {}弧度, = {}角度'.format(tmp, tmp * 180 / pi))

    pairs = [(random_vector_of_length(3), random_vector_of_length(7))
             for i in range(0, 3)]
    for u, v in pairs:
        print("u = %s, v  = %s" % (u, v))
        print("length of u: %f, length of v: %f, dot product :%f" %
              (length(u), length(v), dot(u, v)))
