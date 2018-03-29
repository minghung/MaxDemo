"""
datetime.date.today()
datetime.date(2018,3,27)
datetime.date.today().year
datetime.date.today().month
datetime.date.today().day
"""
import datetime

Mon=["Mon"]
Tue=["Tue"]
Wed=["Wed"]
Thu=["Thu"]
Fri=["Fri"]
Sat=["Sat"]
Sun=["Sun"]
def InputAry(dayNum,WeekDayNum):
     
    if WeekDayNum==0:
        Mon.append(str(dayNum).rjust(3))
    elif WeekDayNum==1:
        Tue.append(str(dayNum).rjust(3))
    elif WeekDayNum==2:
        Wed.append(str(dayNum).rjust(3))
    elif WeekDayNum==3:
        Thu.append(str(dayNum).rjust(3))
    elif WeekDayNum==4:
        Fri.append(str(dayNum).rjust(3))
    elif WeekDayNum==5:
        Sat.append(str(dayNum).rjust(3))
    else:
        Sun.append(str(dayNum).rjust(3))

    if dayNum==1:
        for i in range(WeekDayNum):
            InputAry(" ",i)  
        
begin=datetime.date(2018,3,1)
beginweekday=begin.weekday()

InputAry(begin.day,begin.weekday())
delta=datetime.timedelta(days=1)
begin+delta
for i in range(30):
    begin +=delta
    InputAry(begin.day,begin.weekday())

d1=iter(Mon)
d2=iter(Tue)
d3=iter(Wed)
d4=iter(Thu)
d5=iter(Fri)
d6=iter(Sat)
d7=iter(Sun)


print(next(d1)+" "+next(d2)+" "+next(d3)+" "+next(d4)+" "+next(d5)+" "+next(d6)+" "+next(d7))
print(next(d1)+" "+next(d2)+" "+next(d3)+" "+next(d4)+" "+next(d5)+" "+next(d6)+" "+next(d7))
print(next(d1)+" "+next(d2)+" "+next(d3)+" "+next(d4)+" "+next(d5)+" "+next(d6)+" "+next(d7))
print(next(d1)+" "+next(d2)+" "+next(d3)+" "+next(d4)+" "+next(d5)+" "+next(d6)+" "+next(d7))
print(next(d1)+" "+next(d2)+" "+next(d3)+" "+next(d4)+" "+next(d5)+" "+next(d6)+" "+next(d7))
"""print(next(d1)+" "+next(d2)+" "+next(d3)+" "+next(d4)+" "+next(d5)+" "+next(d6)+" "+next(d7))"""












