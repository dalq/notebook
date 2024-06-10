# 访问定义在闭包内的变量


def sample():
    n = 0
    # 闭包
    def func():
        print('n=', n)

    # 访问闭包中的n变量
    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    func.get_n = get_n
    func.set_n = set_n

    return func


f = sample()
f()
f.set_n(10)
f()
print(f.get_n())