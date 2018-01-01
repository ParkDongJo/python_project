import datetime

# {0:월, 1:화, 2:수, 3:목, 4:금, 5:토, 6:일}
year = 2002
month = 6
day = 1

def getDayName(a,b):
	return ['MON','TUE','WED','THU','FRI','SAT','SUN'][datetime.date(year, a, b).weekday()]
# print(getDayName(month,day))

def getDayIdx(y,m,d):
    return datetime.date(y, m, d).weekday()


target = (6 - getDayIdx(year,month,day) + 4)

print(target)
print(getDayName(month,target+day))

str = str(14)
str = str.zfill(2)
# print(str)

cnt = 0
for i in range(day,14):
    if getDayIdx(year, month, i) == 3:
        cnt += 1
        if cnt == 2:
            print(i)

