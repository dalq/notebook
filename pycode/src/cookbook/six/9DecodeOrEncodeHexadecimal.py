# 编码、解码十六进制数字
import binascii

s = b'hello'
h = binascii.b2a_hex(s)
print(h)

ss = binascii.a2b_hex(h)
print(ss)