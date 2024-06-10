# 在字符串的开头或结尾处做文本匹配
filename = 'spam.txt'
print(filename.endswith('txt'))

filenames = ['1.java', '2.c', '3.java', '4.py']
result = [name for name in filenames if name.endswith('java')]
print(result)

# 必须用元组作为endwith的输入！
# result = [name for name in filenames if name.endswith('java', 'c')]
result = [name for name in filenames if name.endswith(('java', 'c'))]
print(result)
