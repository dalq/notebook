# 移出重复项且元素间顺序不变
# 用set解决


def deldup(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
#yield的理解：生成器可迭代Iterntor
# for循环这一次命中了item，需要对item做一些操作(加入set中)；然后下一步for循环会继续从yield的地方开始


a = [1, 2, 3, 4, 5, 7, 4, 21, 1, 2, 4, 5, 7]
b = list(deldup(a))
print(b)
