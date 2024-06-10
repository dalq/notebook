# 将字典转换为XML
from xml.etree.ElementTree import Element, tostring


def dict_to_xml(tag, d):
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem


s = {'name': 'Good', 'shares': 100, 'price': 490.1}
e = dict_to_xml('stock', s)
print(tostring(e))