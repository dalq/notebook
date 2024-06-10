# 实现自定义的容器
# collections库中定义了各种各样的抽象基类，可以用来实现我们自定义的容器类
import collections, bisect #bisect模块可以让列表中的元素保持有序

class A(collections.Iterable):
    pass


# 自定义实现一个可以排序的sequence
class SortedItems(collections.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is not None else []

    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    def add(self, other):
        bisect.insort(self._items, other)


items = SortedItems([5, 3, 13])
print(list(items))
print(items[0])
items.add(2)
print(items[0])
print(list(items))
