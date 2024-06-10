# 在文本中处理HTML和XML
import html
s = 'Elements are written as "<tag>text</tag>". '
print(s)
print(html.escape(s))

# 双引号不转义
print(html.escape(s, quote=False))

# 反解析这些文本时候，需要使用合适的HTML或XML
