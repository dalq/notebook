# 用函数替代只有单个方法的类
# 需要额外的状态给函数时，考虑使用闭包
from urllib.request import urlopen


def urltemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))
    return opener

yahoo = urltemplate('http://finance.yahoo.com/d/quotes.csv?s={name}&f={fields}')
for line in yahoo(name='IBM,APPL,FB', fields='sllclv'):
    print(line.decode('utf-8'))