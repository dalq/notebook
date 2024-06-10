# 数据汇总和统计 - 使用pandas库
import pandas

stocks = pandas.read_csv('res/stocks.csv')
print(stocks)
print()

# distinct
print(stocks['date'].unique())
print()

# where
print(stocks[stocks['change'] == 0.12])
print()

# order rank
print(stocks['volume'].value_counts()[:2])
print()

# group by
time = stocks.groupby('time')
print(len(time))
print()

# count
time_counts = time.size()
print(time_counts[0:10])
print()

# sort
# time_counts.sort()
# print(time_counts[-10:])

