# %I = 12 hours
# %H = 24 hours
# %M = minute
# %S = second
# %p = AM or PM
# %Y = year 4 digit
# %m = month
# %d = date
# %A = day i.e sunday - saturday

from datetime import datetime
def time_conversion(s):
    # s = hh:mm:ssAM or PM
    time_obj = datetime.strptime(s, '%I:%M:%S%p')
    return time_obj.strftime('%H:%M:%S')

print(time_conversion('07:05:45PM'))


now = datetime.now()
print(now)

format_date = now.strftime('%Y-%m-%d %H:%M:%S')
print(format_date)

date_str = "21 June, 2018"
date_obj = datetime.strptime(date_str, '%d %B, %Y')
print("Parsed date:", date_obj)
formatted_date = date_obj.strftime('%A, %d %B %Y')
print("Formatted date:", formatted_date)