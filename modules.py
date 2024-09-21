#1/6 intro
# Import datetime from datetime below:
from datetime import datetime
current_time = datetime.now()
print(current_time)

#2/6 random module
# Import random below:
import random

# Create random_list below:
random_list = [random.randint(1, 101) for i in range(101)]
print(random_list)

# Create randomer_number below:
randomer_number = random.choice(random_list)

# Print randomer_number below:
print(randomer_number)

#3/6 namespaces 
import codecademylib3_seaborn
from matplotlib import pyplot as plt
import random

# Add your code below:
numbers_a = range(1, 13)
numbers_b = random.sample(range(1000), 12)
print(numbers_b)
plt.plot(numbers_a, numbers_b)
plt.show()

#4/6 decimal modules
# Import Decimal below:
from decimal import Decimal

# Fix the floating point math below:
two_decimal_points = Decimal('0.2') + Decimal('0.69')
print(two_decimal_points)

four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)

#5/6 files and scope
# Import library below:
from library import always_three

# Call your function below:
always_three()

#6/6 review
"""
- what modules are and how they can be useful
- how to use a few of the most commonly used Python libraries
- what namespaces are and how to avoid polluting your local namespace
- how scope works for files in Python
"""