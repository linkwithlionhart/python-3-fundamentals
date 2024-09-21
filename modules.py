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

