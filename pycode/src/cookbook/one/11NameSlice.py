#减少硬编码的索引值

record = '...100...513.2...'
cost = int(record[3:6]) * float(record[9:14])
print(cost)
print(record[3:6])
print(record[9:14])

#change to this
SHARE = slice(3, 6)
PRICE = slice(9, 14)
cost = int(record[SHARE]) * float(record[PRICE])
print(cost)
print(SHARE.start)
print(SHARE.stop)
