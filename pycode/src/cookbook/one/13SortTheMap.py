# 对map排序，根据某些key
from operator import itemgetter

rows = [
    {'name': 'qdl', 'city': 'hz', 'age': 18},
    {'name': 'qqq', 'city': 'us', 'age': 20},
    {'name': 'qer', 'city': 'sh', 'age': 30},
    {'name': 'qop', 'city': 'zb', 'age': 9}
]

rows_by_name = sorted(rows, key=itemgetter('name'))
rows_by_age = sorted(rows, key=itemgetter('age'))

print(rows_by_name)
print(rows_by_age)

# 还可以传入多个key，类似于SQL中group by 两个字段
# 底层是返回两个key联结的元祖
# 性能上itemgetter比lambda要好
