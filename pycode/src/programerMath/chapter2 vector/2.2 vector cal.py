from vector_drawing import *


def add(v1, v2):
    return v1[0] + v2[0], v1[1] + v2[1]


# 所有向量各自的x坐标和y坐标相加
def add2(*vectors):
    return sum([v[0] for v in vectors]), sum([v[1] for v in vectors])


def subtract(v1, v2):
    return v1[0] - v2[0], v1[1] - v2[1]


# 计算向量的长度（勾股定理）
def length(v):
    return sqrt(v[0] ** 2 + v[1] ** 2)


# 距离就是两个输入向量之差的长度
def distance(v1, v2):
    return length(subtract(v1, v2))


# 定义平移向量
def translate(translation, vectors):
    return [add(translation, v) for v in vectors]


# 画100个恐龙
def hundred_dinos():
    translations = [(12 * x, 10 * y)
                    for x in range(-5, 5)
                    for y in range(-5, 5)]
    dinos = [Polygon(*translate(t, dino_vectors), color=blue) for t in translations]
    draw(*dinos, grid=None, axes=None, origin=None)


if __name__ == '__main__':
    dino_vectors = [(6, 4), (3, 1), (1, 2), (-1, 5), (-2, 5), (-3, 4), (-4, 4),
                    (-5, 3), (-5, 2), (-2, 2), (-5, 1), (-4, 0), (-2, 1), (-1, 0), (0, -3),
                    (-1, -4), (1, -4), (2, -3), (1, -2), (3, -1), (5, 1)
                    ]
    dino_vectors2 = [add(v, (1, 0)) for v in dino_vectors]
    draw(Points(*dino_vectors, color=blue),
         Polygon(*dino_vectors, color=blue),
         Points(*dino_vectors2, color=red),
         Polygon(*dino_vectors2, color=red))

    print(length((3, 4)))
    print(add2((1, 2), (3, 4)))

    hundred_dinos()

    # 暴力法找与（1， -1）距离为13的向量（n，m）：n>m>0
    for n in range(-12, 15):
        for m in range(-14, 13):
            if distance((n, m), (1, -1)) == 13 and n > m > 0:
                print(f'暴力查找结果为: {(n, m)}')
