# from datetime import datetime, timedelta
#
# d1 = datetime.now()
# d2 = datetime(2021, 6, 1)p
# diff = d1 - d2
# print(diff)
#
# t = timedelta(weeks=0)
# print(d1 + t)
#
# date_from_str = datetime.strptime("02/02/07 16:10:2", "%m/%d/%y %H:%M:%S")
# print(date_from_str.hour)
# print(d1.strftime("%A %d, %B %y"))
# time = [1,2,3]
# def gen():
#     count=0
#     while time:
#         yield  count
#         count = count + 1
#     for i in gen():
#         print(i)

def counter(low, high, step=1):
    while low < high:
        yield low
        low += step


for i in counter(2, 10):
    print(i)

print(list(counter(2, 6, 2)))
import collections

c1 = collections.Counter("OLAYINKA OLUWATOBI")
print(c1)
c2 = collections.Counter("hi you")
print(c2)
c1.subtract(c2)
print(c1)

person = collections.namedtuple("person", "name age")

p1 = person(name="olayinka", age=17)
print(p1.name)