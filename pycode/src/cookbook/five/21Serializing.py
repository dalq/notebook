# 序列化Python对象
import pickle
from tempfile import TemporaryFile, TemporaryDirectory

data = [1, 2, 3, 4, 5]

# template file 不能序列化？
# with TemporaryFile('wb') as f:
#     pickle.dump(f, 'wb')
#     data = f.read()
#     print(data)

f1 = open('serializefile', 'wb')
pickle.dump(data, f1)

f2 = open('serializefile', 'rb')
print(pickle.load(f2))