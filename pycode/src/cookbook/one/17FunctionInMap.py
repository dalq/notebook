# 创建一个字典，其本身是另一个字典的子集
prices = {
    'ACME': 45.34,
    'AAPL': 612,
    'IBM': 205.09,
    'HPO': 37.2,
    'FB': 10.75
}

p1 = {key: value for key, value in prices.items() if value > 200}
print(p1)
# 这样运行，比元组要快