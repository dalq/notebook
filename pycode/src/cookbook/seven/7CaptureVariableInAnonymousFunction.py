# 在匿名函数中绑定变量的值

x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y

print(a(10))
print(b(10))

# 匿名函数在定义的时候绑定变量，并且保持值不变
x1 = 10
a1 = lambda y, x=x1: x + y
x1 = 20
b1 = lambda y, x=x1: x + y

print(a1(10))
print(b1(10))
print('======================')


funcs = [lambda x : x+n for n in range(5)]
for f in funcs:
    print(f(0))

print('======================')
funcs = [lambda x, n=n : x+n for n in range(5)]
for f in funcs:
    print(f(0))