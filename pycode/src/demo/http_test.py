from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs


# https://zhuanlan.zhihu.com/p/649940378 BaseHTTPRequestHandler 也OK？
class Request(SimpleHTTPRequestHandler):
    timeout = 5
    server_version = 'Apache'

    def do_GET(self):
        self.send_response(200)
        self.send_header("type", "get")  # 设置响应头，可省略或设置多个
        self.end_headers()

        query = parse_qs(urlparse(self.path).query)
        a = int(query.get('a', [0])[0])
        b = int(query.get('b', [0])[0])
        c = a + b
        msg = f"a + b = {c}"
        msg_encoded = msg.encode()
        self.wfile.write(msg_encoded)

    def evaluate(multiproduct_payed_status, opp_product_code_list):
        # 如果 string1 为空，则所有标识符的结果都为 "n"
        if not multiproduct_payed_status:
            return "&&".join([item.split(":")[0] + "_n" for item in opp_product_code_list.split(";")])

        # 将 string1 拆分为元素集合
        string1_elements = set(multiproduct_payed_status.split("&&"))

        # 初始化结果列表
        result_items = []

        # 遍历 string2 中的每一组数据
        for pair in opp_product_code_list.split(";"):
            # 分割标识符和其后面的元素
            key, value = pair.split(":")
            # 将元素拆分为列表
            values = value.split(",")
            # 修改点：如果 string2 中标识符后的任一元素出现在 string1 中
            result = "y" if any(item in string1_elements for item in values) else "n"
            # 将结果添加到列表中
            result_items.append(f"{key}_{result}")

        # 返回连接后的结果字符串
        return "&&".join(result_items)


if __name__ == '__main__':
    # host = ('localhost', 8888)
    # server = HTTPServer(host, Request)
    # server.serve_forever()
    result = Request.evaluate('be524&&be525', 'o1:be525;o2:be485,be524')
    print(result)
