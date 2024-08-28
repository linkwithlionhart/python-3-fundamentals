#1/14
heights = [61, 70, 67, 64, 65]
print(heights)

broken_heights = [65, 71, 59, 62]
print(broken_heights)

#2/14 lists can contain multiple data types
ints_and_strings = [1, 2, 3, "four", "five", "six"]
sam_height_and_testscore = ["Sam", 67, 85.5, True]


#3/14
my_empty_list = []

#4/14 lists have built-in methods
example_list = [1, 2, 3, 4]

#Using Append
example_list.append(5)
print(example_list)

#Using Remove
example_list.remove(5)
print(example_list)

#5/14 list.append()
orders = ["daisies", "periwinkle"]
print(orders)
orders.append("tulips")
orders.append("roses")
print(orders)

#6/14 concatenating lists with '+'
orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]

# Create new orders here:
new_orders = ["lilac", "iris"]
orders_combined = orders + new_orders
print(orders_combined)

broken_prices = [5, 3, 4, 5, 4] + [4]

#7/14 accessing list values
employees = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]

employee_four = employees[3]
print(employee_four)
print(employees[5])

#8/14 accessing list values with negative integers
shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]

last_element = shopping_list[-1]
print(last_element)
index5_element = shopping_list[5]
print(index5_element)

#9/14 modify list elements
# Your code below:
garden_waitlist = ["Jiho", "Adam", "Sonny", "Alisha"]
garden_waitlist[1] = "Calla"
print(garden_waitlist)
garden_waitlist[-1] = "Alex"
print(garden_waitlist)

#10/14 list.remove()
# Your code below: 
order_list = ["Celery", "Orange Juice", "Orange", "Flatbread"]
print(order_list)
order_list.remove("Flatbread")
print(order_list)

new_store_order_list = ["Orange", "Apple", "Mango", "Broccoli", "Mango"]
print(new_store_order_list)
new_store_order_list.remove("Mango")
print(new_store_order_list)
#new_store_order_list.remove("Onions")


#11/14 2D lists
heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64], ["Vik", 68]]

ages = [["Aaron", 15], ["Dhruti", 16]]

#12/14 accessing 2D lists
#Your code below:
class_name_test = [
  ["Jenny",	90],
  ["Alexus",	85.5],
  ["Sam",	83],
  ["Ellie", 101.5]
]

print(class_name_test)
sams_score = class_name_test[2][1]
print(sams_score)
ellies_score = class_name_test[-1][-1]
print(ellies_score)

#13/14 modifying 2D lists
#Your code below:
incoming_class = [
  ["Kenny",	"American",	9],
  ["Tanya",	"Ukrainian",	9],
  ["Madison",	"Indian",	7],
]
print(incoming_class)
incoming_class[2][2] = 8
print(incoming_class)
incoming_class[-3][-3] = "Ken"
print(incoming_class)


#14/14 review
# Your code below: 
first_names = ['Ainsley', 'Ben', 'Chani', 'Depak']

preferred_size = ['Small', 'Large', 'Medium']
preferred_size.append('Medium')
print(preferred_size)

customer_data = [
  ["Ainsley",	"Small",	True],
  ["Ben",	"Large",	False],
  ["Chani",	"Medium",	True],
  ["Depak",	"Medium",	False]
]

print(customer_data)
customer_data[-2][-1] = False
customer_data[1].remove(False)

customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]

print(customer_data_final)

