from datetime import datetime as dt
from decimal import Decimal
from random import randint, choice
import custom_module

date = dt.strftime(dt.now(), '%b %d, %Y')
time = dt.strftime(dt.now(), '%I:%M%p')
print(f"The date is {date}. The time  is {time}.")