#感觉就是SQL中的group by
from operator import itemgetter
from itertools import groupby


rows = [
    {'name': 'qdl', 'city': 'hz', 'age': 18},
    {'name': 'qqq', 'city': 'us', 'age': 20},
    {'name': 'qer', 'city': 'sh', 'age': 30},
    {'name': 'qop', 'city': 'zb', 'age': 18}
]
rows.sort(key=itemgetter('age'))

# 这里是先排序然后group by，可能是为了后续方便分析
for age, items in groupby(rows, key=itemgetter('age')):
    print(age)
    for i in items:
        print(' ', i)