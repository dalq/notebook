# 给字符串中的变量名做差值处理
# 类似于java中的MessageFormat
s = '{name} has {n} message'
a = s.format(name = 'dalq', n = 6)
print(a)


# format_map可以事先定义好变量
name = 'jerry'
n = 3
b = s.format_map(vars())
print(b)

# 可以将变量定义到一个类中
class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n


a = Info('tom', '9')
c = s.format_map(vars(a))
print(c)

# 首选推荐format！
# 对其、填充、数值格式化等