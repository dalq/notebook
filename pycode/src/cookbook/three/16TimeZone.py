# 处理时区相关问题
# pytz模块
from datetime import datetime
from pytz import timezone, country_timezones

d = datetime(2018, 10, 20, 0, 0, 0)
print(d)

us_time = timezone('US/Central').localize(d)
print(us_time)

beijing_time = us_time.astimezone(timezone('Asia/Shanghai'))
print(beijing_time)

print(country_timezones['IN'])