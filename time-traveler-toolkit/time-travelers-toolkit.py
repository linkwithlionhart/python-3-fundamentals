from datetime import datetime as dt
from decimal import Decimal
from random import randint, choice
from custom_module import generate_time_travel_message

today = dt.strftime(dt.now(), '%b %d, %Y')
time = dt.strftime(dt.now(), '%I:%M%p')
print(f"Today's date is {today} at {time}.")

target_year = dt.now().year + randint(100, 1001)
print(f"The target year is {target_year}.")

base_cost = Decimal('777.77')
cost_multiplier = abs(dt.now().year - target_year)
final_cost = round(base_cost * cost_multiplier, 2)
print(f'Total cost to travel to year {target_year} from {today} is ${final_cost}.')

destintations = ['Pandora', 'Mandalore', 'Mars', 'Jhoto', 'Eldia']
destination = choice(destintations)
print(f'Your destination is to {destination}. Ready?')

print(generate_time_travel_message(target_year, destination, final_cost))