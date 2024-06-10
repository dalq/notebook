# 对已不存在的文件执行写入操作
# xt模式在写入之前会检查，如果存在文件，则报错
with open('samplefile.txt', 'xt') as f:
    f.write("not exists")