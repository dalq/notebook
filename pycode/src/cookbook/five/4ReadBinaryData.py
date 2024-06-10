# 读写二进制数据
# rb、wb模式
with open('samplefile.txt', 'rb') as f:
    data = f.read()
print(data)