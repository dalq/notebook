# 处理数据的管道：大批量的数据处理(不能一次读取到内存中)

import os
import fnmatch
import gzip
import bz2
import re


def gen_find(filepat, top):
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)


def gen_opener(filenames):
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        yield f
        f.close()


# 将嵌套的循环中的元素拍平
# see 14FlatteningANestedSequence.py
def gen_concatenate(iterators):
    for it in iterators:
        yield from it


def gen_grep(pattern, lines):
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line


filename = gen_find('sample*', '.')
# 打开匹配的文件们
files = gen_opener(filename)
# 将输入序列拼接成一个很长的行序列
lines = gen_concatenate(files)
# 迭代拍平后的iterator，并进行匹配
pylines = gen_grep('(?i)hello', lines)
for line in pylines:
    print(line)

# yield：生产者；for循环：消费者
