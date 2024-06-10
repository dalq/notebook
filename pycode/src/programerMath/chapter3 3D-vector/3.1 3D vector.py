from draw3d import *

if __name__ == '__main__':
    draw3d(
        Points3D((2, 2, 2), (1, -2, -2)),
        Arrow3D((2, 2, 2)),
        Arrow3D((1, -2, -2)),
        Segment3D((2, 2, 2), (1, -2, -2)),
        Box3D(2, 2, 2),
        Box3D(1, -2, -2),
    )

    pm1 = [1, -1]
    vertices = [(x, y, z) for x in pm1 for y in pm1 for z in pm1]
    edges = [((-1, y, z), (1, y, z)) for y in pm1 for z in pm1] + \
            [((x, -1, z), (x, 1, z)) for x in pm1 for z in pm1] + \
            [((x, y, -1), (x, y, 1)) for x in pm1 for y in pm1]
    draw3d(
        Points3D(*vertices, color=blue),
        *[Segment3D(*edge, color=green) for edge in edges]
    )
