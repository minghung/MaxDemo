import sys
import datetime

today = datetime.date.today()

if "-h" in sys.argv:
    print("python MingCal.py [-h] [month] [year]")
    sys.exit()

if len(sys.argv) < 2:
    today_month = today.month
    today_year = today.year
else:
    today_month = int(sys.argv[1])
    today_year = int(sys.argv[2])


first_day = datetime.date(today_year, today_month, 1)
first_day_weekday = first_day.weekday()+1

month_of_next_month = (today_month+1) % 12
year_of_next_month = (today_month+1) // 12 + today_year

days = (datetime.date(year_of_next_month, month_of_next_month, 1) - first_day).days

print("Sun Mon Tue Wed Thu Fri Sat")

#calc how many space to skip for the first day
if first_day_weekday != 7:
    s = " " * (first_day_weekday * 4)
    print(s, end="")

for i in range(1, days+1):
    print("%3d " % i, end="")
    if (first_day_weekday+i) %7 == 0:
        print()

