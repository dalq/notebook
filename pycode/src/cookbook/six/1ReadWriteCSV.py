# 读写CSV数据
import csv
from datetime import datetime

# 普通方式
with open('./res/stocks.csv') as f1:
    f_csv = csv.reader(f1)
    header = next(f_csv)
    print('header is ', header)
    for row in f_csv:
        print(row)

# 字典序列方式
with open('./res/stocks.csv') as f2:
    f_csv = csv.DictReader(f2)
    for row in f_csv:
        print(row['change'])

# 写入CSV文件
now = datetime.today().strftime('%H:%M:%S%p')
headers = ['symbol', 'price', 'date', 'time', 'change', 'volume']
rows = [('AA', '39.48', '6/11/2007', now, '-0.18', '181800'),
        ('AIG', '71.38', '6/11/2007', now, '-0.15', '195500'),
        ('BA', '98.31', '6/11/2007', now, '0.12', '104800')]
with open('./res/stocks.csv', 'w') as f3:
    f_csv = csv.writer(f3)
    f_csv.writerow(headers)
    f_csv.writerows(rows)
