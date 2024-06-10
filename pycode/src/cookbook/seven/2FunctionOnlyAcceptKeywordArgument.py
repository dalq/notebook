# 只接收关键词参数的函数：必须要使用=传入
# 提高代码的可读性


def recv(maxsize, *, block):
    'Receive a message'
    pass


#recv(1024, True)
recv(1024, block=True)

