"""
根據今天的日期顯示這個月的月曆
"""
import datetime
"""
import datetime
datetime.date.today()
datetime.date(2018,3,27)
datetime.date.today().year
datetime.date.today().month
datetime.date.today().day
begin=datetime.date(2018,3,1)
beginweekday=begin.weekday()
delta=datetime.timedelta(days=1)
d1=iter(Mon)
print(next(d1))
"""


'透過今天取得當月第一天與最後一天'

today=datetime.date.today()

'取得當月第一天'
firstDay=datetime.date(today.year,today.month,1)

'由當月第一天推算次月第一天'
if (firstDay.month+1) > 12 :
    NextMonth=(firstDay.month+1)%12
    NextYear=today.year+((firstDay.month+1)//12)
    LastDay=datetime.date(NextYear,NextMonth,1)
else:
    NextMonth=(today.month+1)%13
    NextYear=today.year
    LastDay=datetime.date(NextYear,NextMonth,1)

'取得當月天數'
DayNum=(LastDay-firstDay).days
DayAry=range(1,DayNum+1)


'確認當月第一天的weekday'
firstDayWeekDay=firstDay.weekday()
NoInMonth=""

'顯示月曆'
print(today.year,today.month,"的月曆")
print("Mon Tur Wed Tru Fri Sat Sun")
dayitem=iter(DayAry)
wc=1
for i in range(0,DayNum+firstDayWeekDay):
    if i < firstDayWeekDay:
        print(str(NoInMonth).rjust(3)+" ",end="")
    else:
        if wc%7>0: 
            print(str(next(dayitem)).rjust(3)+" ",end="")
        else:
            print(str(next(dayitem)).rjust(3)+"\n")            
    wc +=1




