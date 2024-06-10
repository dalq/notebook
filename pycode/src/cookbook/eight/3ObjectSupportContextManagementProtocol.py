# 让对象支持上下文管理协议
# 通过with语句触发

# 需要实现__enter__()和__exit__()方法

from socket import socket, AF_INET, SOCK_STREAM
from functools import partial


class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = AF_INET
        self.type = SOCK_STREAM
        self.sock = None

    # 遇到with语句时，__enter__方法先被触发执行，它的返回值防止在由as限定的变量中
    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    # 执行with代码块中的语句
    # 最后__exit__被触发来执行清理工作
    def __exit__(self, exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None


conn = LazyConnection(('www.python.org', 80))
# Connection closed
with conn as s:
    # conn.__enter__() executes: connection open
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))
    print(resp)
