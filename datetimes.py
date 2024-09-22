"""
Key concepts:
- datetime module
- strptime()
- strftime()
"""
# importing  the 'datetime' module
from datetime import datetime

# creating a date using year, month, day as arguments
birthday = datetime(1992, 1, 27, 4, 25, 12)
print(birthday.year)
print(birthday.month)
print(birthday.day)
print(birthday.hour)
print(birthday.weekday())

# creating a date using datetime.now()
print(datetime.now())
print(datetime(2018, 1, 1) - datetime(2017, 1, 1))
print(datetime.now() - datetime(2018, 1, 1))

# parsing a date using strptime
parsed_date = datetime.strptime('Jan 15, 2018', '%b %d, %Y')
print(parsed_date.month)
print(parsed_date.year)

# rendering a date as a string using strftime
date_string = datetime.strftime(datetime.now(), '%b %d, %Y')
print(date_string)