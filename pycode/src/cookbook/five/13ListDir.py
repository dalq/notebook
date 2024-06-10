# 获取某个目录下包含的文件列表
import os
import glob

names = os.listdir('/usr')
print(names)

names2 = [name for name in os.listdir('/tmp')
          if name.endswith('log')]
print(names2)



name_size_collection = [(name, os.path.getsize(name), os.path.getmtime(name))
                        for name in glob.glob('/tmp/*.log')]
for name, size, mtime in name_size_collection:
    print(name, size, mtime)