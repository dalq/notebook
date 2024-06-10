# 从字节串中打包和解包大整数
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
print(len(data))
res = int.from_bytes(data, 'little')
print(res)
res = int.from_bytes(data, 'big')
print(res)