# 将元数据信息附加到函数参数上
# 只是丰富了一下文档内容而已，因为python中没有类型声明这一说


def add(x:int, y:int) -> int:
    return x + y


print(add(1, 2))
print(add.__annotations__)