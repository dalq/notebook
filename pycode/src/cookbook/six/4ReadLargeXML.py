# 以增量方式解析大型XML文件

from xml.etree.ElementTree import parse, iterparse
from collections import Counter
#from guppy import hpy

# 方法一：浪费内存
potholes_by_zip = Counter()
doc = parse('./res/stocks.xml')
for pothole in doc.iterfind('channel/item'):
    potholes_by_zip[pothole.findtext('zip')] += 1
for zipcode, num in potholes_by_zip.most_common():
    print(zipcode, num)
#print profile.heap()


# 方法二：节省内存


def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))
    # Skip the root element
    next(doc)

    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
                elem_stack[-2].remove(elem)
        try:
            tag_stack.pop()
            elem_stack.pop()
        except IndexError:
            pass


# todo why it doesn't work
potholes_by_zip_2 = Counter()
data = parse_and_remove('./res/stocks.xml', 'channel/item')
for pothole in data:
    potholes_by_zip_2[pothole.findtext('zip')] += 1
for zipcode, num in potholes_by_zip_2.most_common():
    print(zipcode, num)
#print profile.heap()