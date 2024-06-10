# 可接受变参数的函数
# 位置参数？ - tuple；关键字参数？ - dict
import html


def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))


print(avg(1, 2))
print(avg(1, 2, 3, 4))


def make_element(name, value, **attrs):
    #将map格式化为这种格式
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(name=name, attrs=attr_str, value=html.escape(value))
    return element


print(make_element('item', 'Albatross', size='large', quantity=6))
