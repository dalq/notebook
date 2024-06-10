#实现一个优先级队列
import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # 所以heappush的入参是一个list
        heapq.heappush(self._queue, (-priority, self._index, item))
        # 每放入一个item，都会有一个固定的list中的索引_index，这样即使优先级一样，但是联合索引肯定是不一样的，就可以排序了！
        # 元祖的概念？
        # 放的不是一个对象，而是一个元组：(优先级+索引+对象)！
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    # repr 将一个subject转化为供解释器读取的形式(String)
    def __repr__(self):
        # todo what's this? (0073BF)
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
