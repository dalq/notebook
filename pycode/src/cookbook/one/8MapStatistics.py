# map值的计算
prices = {
    'ACME': 45.23,
    'APL': 23,
    'HQP': 37.2,
    'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
print(min_price)

sorted_price = sorted(zip(prices.values(), prices.keys()))
print(sorted_price)

# 如果直接对于value操作min室可以的，但是会把key信息丢掉
print(min(prices.values()))
