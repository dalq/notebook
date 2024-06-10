# 找出当月的日期范围
from datetime import datetime, timedelta, date
import calendar

start_date = date.today().replace(day=1)
# 返回的是一个元组y
_, days_in_month = calendar.monthrange(start_date.year, start_date.month)
end_date = start_date + timedelta(days=days_in_month)

while start_date < end_date:
    print(start_date)
    start_date += timedelta(days=1)