# 对序列list中的元素做运算
myList = [1, 2, 4, -5, 6, -7, 8, -9]
pos = (n for n in myList if n > 0)
# 这样打印出来的是地址
print(pos)
for x in pos:
    print(x)


# 还可以自定义函数，然后使用list的filter接口
def is_small_than_zero(val):
    return val < 0


pos2 = list(filter(is_small_than_zero, myList))
for y in pos2:
    print(y)

pos3 = [n if n > 0 else 0 for n in myList]
for z in pos3:
    print(z)