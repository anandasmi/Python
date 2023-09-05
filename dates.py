# DATE OBJECTS

from datetime import date
from datetime import time
from datetime import datetime

# Get todays date from the simple today() method from the date class
today = date.today()
print("Todays date is ", today)

# print out the dates individual components
print("Date Components :", today.day, today.month, today.year)

# retrieve todays weekday (0=monday, 6=sunday)
print("Today's weekday #is", today.weekday)
days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
print("Which is a ", days[today.weekday()])


# DATETIME OBJECTS
# Get todays date from the datetime class
today = datetime.now()
print("Time right now = ", today)

# Get the current time
t = datetime.time(datetime.now())
print("The current time is :", t)
