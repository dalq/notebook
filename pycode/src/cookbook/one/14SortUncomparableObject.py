# 传入回调对象，类似于Java中传入匿名函数，根据某个字段进行排序
from operator import attrgetter


class User:
    def __init__(self, user_id):
        self.user_id = user_id
    def __repr__(self):
        return 'User({})'.format(self.user_id)


users = [User(23), User(3), User(18)]

sorted_user = sorted(users, key=lambda u : u.user_id)
#或者可以使用这个!
#attrgetter
#min的用法
min_user = min(users, key=attrgetter('user_id'))

print(sorted_user)
print(min_user)
