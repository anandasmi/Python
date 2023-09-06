# WORKING WITH CALENDARS

# IMPORT THE CALENDAR MODULE
import calendar

# CREATE A PLAIN TEXT CALENDAR
# c = calendar.TextCalendar(calendar.MONDAY)
# str = c.formatmonth(2002, 1, 0, 0)
# print(str)

# CREATE AN HTML FORMATTED CALENDAR
# hc = calendar.HTMLCalendar(calendar.SUNDAY)
# str = hc.formatmonth(2002, 1)
# print(str)

# LOOP OVER THE DAYS OF A MONTH
# zeros mean that the day of the week is in an overlapping month
# for i in c.itermonthdays(2002, 8):
# print(i)

# The calendar module provides useful utilities for the given locale,
# such as the names of the xays and months in both full and abbreviated forms
# for name in calendar.month_name:
# print(name)

# for day in calendar.day_name:
# print(day)


# Calculate days based on a rule: For example, consider
# a time meeting on the first friday of  every month.
# to figure out what days that would be for each month,
# we can use this script:

print("Team meetings will be on:")
for m in range(1, 13):
    cal = calendar.monthcalendar(2022, m)
    weekone = cal[0]
    weektwo = cal[1]
    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]

    print(calendar.month_name[m], meetday)
