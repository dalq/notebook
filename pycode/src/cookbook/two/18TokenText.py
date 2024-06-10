# 文本分词 - 通过正则中的命名捕获组来实现
import re
text = 'foo = 23 + 42 * 10'
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
scanner = master_pat.scanner('foo = 42')
print(scanner.match())
print(scanner.match())
print(scanner.match())
print(scanner.match())
print(scanner.match())

# todo 搞成一个函数