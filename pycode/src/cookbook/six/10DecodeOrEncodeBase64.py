# base64编码和解码
import base64

# base64编码智能用在面向字节的数据上(例如字节串和字节数组)
s = b'hello'
a = base64.b64encode(s)
print(a)

ss = base64.b64decode(a)
print(ss)

aa = base64.b64encode(s).decode('ascii')
print(aa)