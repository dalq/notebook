# 求集合的交并补
a = {
    'x': 1,
    'y': 2,
    'z': 3
}
b = {
    'w': 9,
    'x': 8,
    'y': 2
}

intersection = a.keys() & b.keys()
union = a.keys() | b.keys()
diff = a.keys() - b.keys()

print(intersection)
print(union)
print(diff)

diff_item = a.items() & b.items()

print(diff_item)