def scale(scalar, v):
    return tuple(scalar * coord for coord in v)


def add(*vectors):
    by_coordinate = zip(*vectors)
    coordinate_sums = [sum(coords) for coords in by_coordinate]
    # [7, 7, -3] --> (7, 7, -3)
    return tuple(coordinate_sums)


# 接收一个标量列表和相同数量的向量，并返回一个向量
def linear_combination(scalars, *vectors):
    scaled = [scale(s, v) for s, v in zip(scalars, vectors)]
    return add(*scaled)


if __name__ == '__main__':
    # 使用 zip 函数将标量列表 [1, 2, 3] 和向量 ((1, 0, 0), (0, 1, 0), (0, 0, 1)) 按照顺序配对，得到一个迭代器，它会产生三个元组：
    # (1, (1, 0, 0))，(2, (0, 1, 0)) 和 (3, (0, 0, 1))。

    # 列表推导式遍历这个迭代器中的每个元组，将每个元组的第一个元素（标量）和第二个元素（向量）作为参数传递给 scale 函数。 对于每一对 (标量, 向量)，
    # scale 函数将向量中的每个坐标乘以标量，得到新的缩放后的向量，然后将它们全部收集到一个列表中。

    # 于是我们得到了三个缩放后的向量：
    # scale(1, (1, 0, 0)) 返回 (1*1, 1*0, 1*0) 即 (1, 0, 0)
    # scale(2, (0, 1, 0)) 返回 (2*0, 2*1, 2*0) 即 (0, 2, 0)
    # scale(3, (0, 0, 1)) 返回 (3*0, 3*0, 3*1) 即 (0, 0, 3)
    # 最终，scaled 列表包含了所有缩放后的向量： [(1, 0, 0), (0, 2, 0), (0, 0, 3)]。

    # 这个列表随后会被 * 操作符解包，并作为参数传递给 add 函数，以计算这些缩放后向量的和。
    # 即(1+0+0, 0+2+0, 0+0+3) = (1, 2, 3)
    res = linear_combination([1, 2, 3], (1, 0, 0), (0, 1, 0), (0, 0, 1))
    print(res)
