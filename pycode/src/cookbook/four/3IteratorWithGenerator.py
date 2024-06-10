# 用生成器创建新的迭代模式
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment

# fixme 生成器如何理解？
# 与普通函数不同，生成器会在响应迭代操作时才运行
for n in frange(0, 4, 0.5):
    print(n)
