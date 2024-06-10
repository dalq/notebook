#从任意长度的可迭代对象中分解元素

record = ('name', 'addr', 'tel', 'tel2')
name, addr, *tel = record
print(name)
print(addr)
print(tel)

*before, after = [1, 2, 3, 4, 5, 6]
print(before)
print(after)

# 在循环中也好使
record = [('foo', 1, 2), ('bar', 'hello'), ('foo', 5, 6)]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *tags in record:
    if tag == 'foo':
        do_foo(*tags)
    elif tag == 'bar':
        do_bar(tags)
