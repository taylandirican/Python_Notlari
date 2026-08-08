# import datetime

# result = dir(datetime)
# print(result)

# result1 = dir(datetime.date)
# print(result1)

from datetime import datetime
from datetime import timedelta

şimdi = datetime.today()
# result = şimdi.day
# result = şimdi.month
# result = şimdi.year
# result = şimdi.hour
# result = şimdi.minute
# result = şimdi.second


# result = datetime.ctime(şimdi)
# result = datetime.strftime(şimdi,"%Y")
# result = datetime.strftime(şimdi,"%X")
# result = datetime.strftime(şimdi,"%d")
# result = datetime.strftime(şimdi,"%a")
# result = datetime.strftime(şimdi,"%b")
# result = datetime.strftime(şimdi,"%Y %b %a")

# print(result)

#https://python-istihza.yazbel.com/standart_moduller/datetime.html


t = "13 June 2008 hour 19:05:25"

# gun, ay , yıl = t.split()
# print(gun)
# print(ay)
# print(yıl)

dt = datetime.strptime(t, "%d %B %Y hour %H:%M:%S" )
dt = dt.month


birthdaybsyza = datetime(2008,6,13,19,5,25)


dt = datetime.timestamp(birthdaybsyza) #saniye
dt = datetime.fromtimestamp(dt)#saniye den datetimwa
dt = datetime.fromtimestamp(0)#bilgisayarlar için milat

dt = şimdi-birthdaybsyza # timedelta


dt = dt.microseconds



dt = şimdi + timedelta(days=10)
print(dt)