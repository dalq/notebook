# 将日转化为秒、将消失转化为分钟
from datetime import timedelta, datetime
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c.days)
print(c.seconds)

x = datetime(2018, 10, 21)
print(x + timedelta(days=10))

print(datetime.today() + timedelta(minutes=10))

# dateutil.relativedelta对于处理日期更加强大(安装python-dateutil包)
# from dateutil.relativedelta import relativedelta
# datetime.datetime(2018, 10, 21) + relativedelta(months=+4, days=+28)