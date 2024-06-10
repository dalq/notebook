# 用名称来替代索引，来访问列表或元组中的元素
from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('daql@dalq.com', '2018-09-02')
print(sub)
print(sub.addr)
print(sub.joined)

addr, joined = sub
print(addr)
print(joined)


# 元组 VS 命名元组
def compute_cost(records):
    total = 0.0
    for rec in records:
        total += records[1] * records[2]
    return records


Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost2(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec) ##todo 类似于java中的省略符号... see 2SplitArbitrarySequence.py
        total += s.shares * s.price
    return total

# 命名元组是immutable的