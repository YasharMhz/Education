
# datetime module
# The datetime module is used to work with dates and times.

from datetime import datetime, timedelta
import time


# Creating a datetime object manually
dt1 = datetime(2025, 4, 2)


# Getting the current date and time
dt2 = datetime.now()


# Converting a string into a datetime object
# %Y = four digit year
# %m = month
# %d = day

dt = datetime.strptime("2011/3/1", "%Y/%m/%d")


# Converting Unix timestamp into datetime
dt = datetime.fromtimestamp(time.time())


# Converting datetime object into string
print(dt.strftime("%y/%m/%d"))


# Comparing two dates

print(dt1 > dt2)


# Accessing datetime attributes

print(dt)
print(dt.year)
print(dt.month)
print(dt.day)


# timedelta
# timedelta is used to calculate differences between dates
# or add/subtract time from a date.

dt1 = datetime(2025, 4, 2) + timedelta(
    days=1,
    seconds=1000
)

dt2 = datetime.now()


# Difference between two dates

duration = dt2 - dt1


print(dt1)


# Difference in days

print(duration.days)


# Remaining seconds after days

print(duration.seconds)


# Complete difference in seconds

print(duration.total_seconds())