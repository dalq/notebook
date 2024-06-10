# 手动访问迭代器中的元素
with open('sample.txt') as f:
    try:
        while True:
            line = next(f)
            print(line, end='')
    # 通知我们迭代结束了
    except StopIteration:
        pass

# 也可以这样：
with open('sample.txt') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')