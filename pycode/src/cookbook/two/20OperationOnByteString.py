# 在字节串上执行文本操作
# 几乎所有能再文本字符串上执行的操作同样也可以在字节串就上进行
data = b'Hello World'
print(data)
print(data[0:5])

d = bytearray(b'Hello World')
print(d)
print(d[0:5])


# 区别
a1 = 'Hello World'
print(a1[0])
a2 = b'Hello World'
print(a2[0])

#如果想对字节串做格式化操作，应该先转为普通的文本字符串然后再做编码
