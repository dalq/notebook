
def vertices(faces):
    # 第一个vertex是输出，第一个for-in是外层循环，第二个for-in是内层循环
    return list(set([vertex for face in faces for vertex in face]))


if __name__ == '__main__':
    octahedron = [
        [(1, 0, 0), (0, 1, 0), (0, 0, 1)],
        [(1, 0, 0), (0, 0, -1), (0, 1, 0)],
        [(1, 0, 0), (0, 0, 1), (0, -1, 0)],
        [(1, 0, 0), (0, -1, 0), (0, 0, -1)],
        [(-1, 0, 0), (0, 0, 1), (0, 1, 0)],
        [(-1, 0, 0), (0, 1, 0), (0, 0, -1)],
        [(-1, 0, 0), (0, -1, 0), (0, 0, 1)],
        [(-1, 0, 0), (0, 0, -1), (0, -1, 0)],
    ]
    a = set([v for face in octahedron for v in face])
    # print(vertices(octahedron))
    print(a)
