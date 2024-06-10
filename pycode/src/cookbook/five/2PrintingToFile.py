# 将输出重定向到文件中
# fixme 应该是wt模式吧？rt报错。
with open('samplefile.txt', 'rt') as f:
    print('Hello World!', file=f)