# 打印无法解码的文件名
# python假设所有的文件名都是根据sys.getfilesystemencoding返回的编码形式进行编码的
# 对于错误的文件名python会打印出unicode字符，程序崩溃