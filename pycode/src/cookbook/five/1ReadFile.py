# 读写文本数据

# wt模式，写文件，会覆盖写；at模式是追加写
with open('samplefile.txt', 'wt') as f:
    f.write('hello')
    f.write('world')

# 读： open函数，rt模式；with语句：读完自动关闭；否则的话需要显示调用close方法
with open('samplefile.txt', 'rt') as f:
    data = f.read()
print(data)

with open('samplefile.txt', 'rt') as f:
    for line in f:
        print(line)

# 换行写
with open('samplefile.txt', 'wt') as f:
    print('write', file=f)
    print('line', file=f)

with open('samplefile.txt', 'rt') as f:
    data = f.read()
print(data)