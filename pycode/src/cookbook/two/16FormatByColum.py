# 以固定的列数重新格式化文本 - textwrap
import textwrap
s = "Look into my eyes, look into my eyes, the eyes, the eyes, " \
    "the eyes, not around the eyes, don't look around the " \
    "eyes, look into my eyes, you're under. "

print(textwrap.fill(s, 70))
print("====================>")
print(textwrap.fill(s, 40))
print("====================>")
print(textwrap.fill(s, 40, initial_indent = '*'))
print("====================>")
print(textwrap.fill(s, 40, subsequent_indent = '*'))
