import os


class ListStudy:

    def __index__(self):
        self.var = ''
        self.lowerVar = ''

    # 列表生成式
    var = [d for d in os.listdir('/Users/quan')]
    print(var)

    lowerVar = [s.lower() for s in var]
    print(lowerVar)

    # 斐波那契数组
    def fib(maxN):
        n, a, b = 0, 0, 1
        while n < maxN:
            print(b)
            a, b = b, a + b
            n = n + 1
        return 'done'
