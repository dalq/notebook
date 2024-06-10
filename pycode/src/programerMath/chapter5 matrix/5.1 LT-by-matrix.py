def dot(u, v):
    return sum([coord1 * coord2 for coord1, coord2 in zip(u, v)])


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


# 矩阵与向量相乘
# matrix矩阵表示形式为元祖的元祖
# vector向量表示形式为元祖
# 在Python中把矩阵定义为行元组的好处是，数的排列顺序和在纸上的书写顺序一样。不过，使用Python的zip函数（附录B中有介绍），可以随时得到列。
def multiply_matrix_vector(matrix, vector):
    return linear_combination(vector, *zip(*matrix))


# 矩阵与矩阵相乘
# 对于矩阵 a 中的每一行 row，我们需要计算它与矩阵 b 中每一列 col 的点积。首先，矩阵 b 需要转置，使得我们可以通过迭代访问其列。在Python中，zip(*b) 表示对矩阵 b 进行转置。
# 外层的 for row in a 循环用于遍历矩阵 a 的每一行。
# 内层的 tuple(dot(row, col) for col in zip(*b)) 循环用于计算当前行 row 与矩阵 b 的每一列 col 的点积，生成一个新的元组，这个元组代表了结果矩阵中的一行。
# 最终，外层循环将所有行组合起来，形成一个包含所有行的元组，这就是结果矩阵。
def matrix_multiply(a, b):
    return tuple(
        # (dot(row, col) for col in zip(*b))将产生一个生成器对象，该对象可以被迭代以产生每次计算的点积值。
        # 为了将这些值保存在一个固定的、不可变的序列中，你需要使用 tuple() 函数将它们转换为一个元组
        tuple(dot(row, col) for col in zip(*b))
        for row in a
    )


if __name__ == '__main__':
    B = (
        (0, 2, 1),
        (0, 1, 0),
        (1, 0, -1)
    )
    v = (3, -2, 5)
    result = multiply_matrix_vector(B, v)
    print(result)

    a = ((1, 1, 0), (1, 0, 1), (1, -1, 1))
    b = ((0, 2, 1), (0, 1, 0), (1, 0, -1))
    c = matrix_multiply(a, b)
    print(c)
