import datetime

c = 0
for year in range(1901,2001):
    for month in range(1,13):
        date = datetime.datetime(year, month, 1)
        weekday = date.strftime("%A")
        if weekday == "Sunday":
            c += 1
print(c)
