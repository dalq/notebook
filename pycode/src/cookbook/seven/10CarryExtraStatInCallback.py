# 在回调函数中携带额外的状态


def apply_async(func, args, *, callback):
    result = func(*args)
    callback(result)


def print_result(result):
    print('Got:', result)


def add(x, y):
    return x + y


apply_async(add, (2, 3), callback=print_result)

apply_async(add, ('hello', 'world'), callback=print_result)


#在回调函数中携带额外信息的方法
# 1、绑定方法 -> 函数换成了类
class ResultHandler:
    def __init__(self):
        self.sequence=0
    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))

r = ResultHandler()
apply_async(add, (2, 3), callback=r.handler)
apply_async(add, ('hello', 'world'), callback=r.handler)

# 2、闭包 -> 用闭包替代单个方法的类
def make_handler():
    sequence = 0
    def handler(result):
        # 表示变量sequence时在回调函数中修改的
        nonlocal sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))
    return handler

handler = make_handler()
apply_async(add, (2, 3), callback=handler)
apply_async(add, ('hello', 'world'), callback=handler)

# 3、协程coroutine ->
def make_handler2():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))

handler2 = make_handler2()
next(handler2)
apply_async(add, (2, 3), callback=handler2.send)
apply_async(add, ('hello', 'world'), callback=handler2.send)
