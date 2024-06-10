# 定义带有默认参数的函数


def spam(a, b=42):
    print(a, b)


spam(1)
spam(1, 2)


_no_value = object()


def spam2(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')
        return
    print(a, b)


spam2(1)


def spam3(a, b=[]):
    # 修改入参！
    # 修改指针了
    print(a, b)
    return b


x = spam3(1)
print(x)
x.append(99)
x.append('Yow!')
print(x)
spam3(1)