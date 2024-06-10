# 随机选择
import random
values = [1, 2, 3, 4, 5, 6]
print(random.choice(values))

random.shuffle(values)
print(values)

print(random.randint(0, 100))

print(random.random())

# 使用的是马特赛特旋转算法，是确定性算法
# 可以random.seed()修改初始种子