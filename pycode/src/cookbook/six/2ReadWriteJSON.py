# 读写JSON数据
import json
from datetime import datetime

now = datetime.today().strftime("%H:%M:%S%p")
data = {
    "name": "dalq",
    "time": now,
    "shares": 100,
    "price": 12.34
}
with open('./res/stocks.json', 'w') as f:
    json.dump(data, f)

with open('./res/stocks.json', 'r') as f:
    data = json.load(f)

print(data)