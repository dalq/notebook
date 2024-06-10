from vector_drawing import *


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 ⌘F8 切换断点。


def greet(name):
    print('hello, %s' % name)


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')
    for i in ['1', '2']:
        greet(i)
    dino_vectors = [(6, 4), (3, 1), (1, 2), (-1, 5), (-2, 5), (-3, 4), (-4, 4),
                    (-5, 3), (-5, 2), (-2, 2), (-5, 1), (-4, 0), (-2, 1), (-1, 0), (0, -3),
                    (-1, -4), (1, -4), (2, -3), (1, -2), (3, -1), (5, 1)
                    ]

    draw(
        Points(*dino_vectors, color=red)
    )
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
