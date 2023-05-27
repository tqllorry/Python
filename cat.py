import time,sys,re
from datetime import date, datetime, timedelta

ds = "20230312"
match = re.match(r"([\d]{4})([\d]{2})([\d]{2})", ds)
daySub = match.group(1, 2, 3)

ds_year = daySub[0]
ds_month = daySub[1]
ds_day = daySub[2]

last_day = datetime(int(daySub[0]), int(daySub[1]), int(daySub[2]))
last_day_str = last_day.strftime('%Y%m%d')
dt_with_separtor = last_day.strftime('%Y-%m-%d')

print('last_day_str=%s' % last_day_str)
print('ds_year=%s' % ds_year)
print('ds_month=%s' % ds_month)
print('ds_day=%s' % ds_day)

last_dt = (last_day + timedelta(days=-1)).strftime("%Y%m%d")
print('last_dt=%s' % last_dt)

yesterday = (date.today() + timedelta(days=-1)).strftime("%Y%m%d")
print('yesterday=%s' % yesterday)