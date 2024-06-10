# 字符串连接以及合并
parts = ['Hello', 'I', 'am', 'dalq!']
print(' '.join(parts))

# + 一般都可以使用formal替代，后者针对更加复杂的字符串格式化操作
# + 的性能是非常低效的：内存拷贝和垃圾收集
a = '1'
b = '2'
c = '3'
print(a + ':' + b + ':' + c) # ugly
print(':'.join([a, b, c])) # ugly
print(a, b, c, sep=':') # better

# todo 如果我们便携的代码要从许多短字符串中构建输出，则应该考虑编写生成器函数
# 通过yield关键字生成字符串片段