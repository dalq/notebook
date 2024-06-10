from draw3d import *
from math import sin, cos, pi


def add(*vectors):
    by_coordinate = zip(*vectors)
    coordinate_sums = [sum(coords) for coords in by_coordinate]
    # [7, 7, -3] --> (7, 7, -3)
    return tuple(coordinate_sums)


def length(v):
    return sqrt(sum([coord ** 2 for coord in v]))


def practice_3_5():
    vs = [(sin(pi * t / 6), cos(pi * t / 6), 1.0 / 3) for t in range(0, 24)]
    # 在(0, 0, 0)处初始化动态和，从这里开始从头到尾相加
    running_sum = (0, 0, 0)
    arrows = []
    for v in vs:
        # 绘制后续首尾相接的向量时，把它加到动态和上。最新的箭头把前一个动态和与下一个连接起来
        next_sum = add(running_sum, v)
        arrows.append(Arrow3D(next_sum, running_sum))
        running_sum = next_sum
    print(running_sum)
    draw3d(*arrows)


def scale(scalar, v):
    return tuple(scalar * coord for coord in v)


def vectors_with_whole_number_length(max_coord=100):
    for x in range(1, max_coord):
        for y in range(1, x+1):
            for z in range(1, y+1):
                if length((x, y, z)).is_integer():
                    yield x, y, z


if __name__ == '__main__':
    print('length((3, 4, 12) = {}'.format(length((3, 4, 12))))
    draw3d(
        Arrow3D((4, 0, 3), color=red),
        Arrow3D((-1, 0, 1), color=blue),
        Segment3D((3, 0, 4), (4, 0, 3), color=blue),
        Segment3D((-1, 0, 1), (3, 0, 4), color=red),
        Arrow3D((3, 0, 4), color=orange)
    )

    vector1 = [(1, 2, 3, 4, 5), (1, 2, 3, 4, 5)]
    vector2 = [(1, 2), (3, 4), (5, 6)]
    zip_vector1 = zip(*vector1)
    zip_vector2 = zip(*vector2)
    print('zip([(1, 2, 3, 4, 5), (1, 2, 3, 4, 5)]) = {}'.format(list(zip_vector1)))
    print('zip([(1, 2), (3, 4), (5, 6)]) = {}'.format(list(zip_vector2)))

    practice_3_5()
    print('scale(2, (1, 2, 3)) = {}'.format(scale(2, (1, 2, 3))))

    # yield返回的是generator类型对象
    practice_3_9 = vectors_with_whole_number_length()
    practice_3_9_list = list(practice_3_9)
    print('vectors_with_whole_number_length find {} results, min = {}, max = {}'.format(len(practice_3_9_list),
                                                                                        practice_3_9_list[0],
                                                                                        practice_3_9_list[-1]))
