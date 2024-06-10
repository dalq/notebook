# 计算上周五的日期
# 使用dateutil会更方便
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *

d = datetime.now()
print(d)

# 下周五
print(d + relativedelta(weekday=FR))
# 上周五
print(d + relativedelta(weekday=FR(-1)))

### 徒手写看起来会是这样的：
dd = datetime.today()

day_num = dd.weekday()
print(day_num)

days_ago = (7 + day_num - 4) % 7
# days_ago = days_ago == 0 ? 7 : days_ago
print(days_ago)

target_dd = dd - timedelta(days=days_ago)
print(target_dd)