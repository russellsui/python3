# Python Dates and Times
# need to import datetime and time
import datetime as dt
import time as tm
print(tm.time()) # this will print out how much time is there from 1970-01-01 to now
dtnow = dt.datetime.fromtimestamp(tm.time())
print(dtnow) # will give the time now
# if we wanna pick the specific element of the time
dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second
# this will print out a tuple
delta = dt.timedelta(days = 100)
# delta actually gives us a days variable, it will be like assign a days 100 to delta
# and then we could use delta to do some numerical operations

# dt.date actully gives us objects of date like yyyy-mm-dd
today = dt.date.today()
print(today)
# here we used the predefined delta to do some numerical calculations
# this will be like throwback 100 days from today and print the result date
print(today - delta)
