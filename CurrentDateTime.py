from datetime import datetime, timedelta

d1 = datetime.now()
d2 = datetime(2021, 6, 1)
diff = d1 - d2
print(diff)

t = timedelta(weeks=0)
print(d1 + t)

date_from_str = datetime.strptime("02/02/07 16:10:2", "%m/%d/%y %H:%M:%S")
print(date_from_str.hour)