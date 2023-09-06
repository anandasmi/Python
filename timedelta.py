# # WORKING WITH THE TIMEDELTA OBJECTS

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# # Construct a basic timedelta and print it
# print(timedelta(days=365, hours=5, minutes=5))

# # print todays date
# now = datetime.now()
# print("Today is", now)

# # print todays date one year from now
# print("One year from now it will be", str(now + timedelta(days=365)))

# # create a timedelta that uses more than one argument
# print("In two weeks and 3 days it will be", str(now + timedelta(weeks=2, days=3)))

# # Calculate the date 1 week agao, formatted as a string
# t = datetime.now() - timedelta(weeks=1)
# s = t.strftime("%A %B %d %Y")
# print("One week ago it was", s)


# ###HOW MANY DAYS UNTIL APRIL FOOLS DAY??
today = date.today()
afd = date(today.year, 4, 1)

# # Use comparison to see if april fools day has already gone or not for this year
# # if it is has, use replace() function to get the date  for next year
if afd < today:
    print("April Fools' Day already went by:", ((today - afd).days))
    afd - afd.replace(year=today.year + 1)

# Now calculate the amount of time until April Fools Day
time_to_afd = afd - today
print("It is", time_to_afd.days, "days until the next April Fools Day!")
