#1/15
  my_name = "William"
  print("Hello and welcome " + my_name + "!")

#2/15
  # Documentation is important.

#3/15
  print("Hello World!")

#4/15
  print('Will')
  print("Will")

#5/15
  # We've defined the variable "meal" here to the name of the food we ate for breakfast!
  meal = "An english muffin"

  # Printing out breakfast
  print("Breakfast:")
  print(meal)

  # Now update meal to be lunch!
  meal = "An asian muffin"

  # Printing out lunch
  print("Lunch:")
  print(meal)

  # Now update "meal" to be dinner
  meal = "A middle eastern muffin"

  # Printing out dinner
  print("Dinner:")
  print(meal)

#6/15
  print('This message has mismatched quote marks!')
  print("Abracadabra")

#7/15
  # Define the release and runtime integer variables below:
  release_year = 2020
  runtime = 120

  # Define the rating_out_of_10 float variable below: 
  rating_out_of_10 = 5.5

#8/15
  print(25 * 68 + 13 / 28)

#9/15
  quilt_width = 8
  quilt_length = 12
  print(quilt_width*quilt_length)
  quilt_length = 8
  print(quilt_width*quilt_length)

#10/15
  # Calculation of squares for:
  # 6x6 quilt
  print(6**2)

  # 7x7 quilt
  print(7**2)

  # 8x8 quilt
  print(8**2)

  # How many squares for 6 people to have 6 quilts each that are 6x6?
  print(6*6*6*6)
  print(6**4)

#11/15
  first_order_remainder = 269 % 10
  print(first_order_remainder)

  first_order_coupon = 'no'

  second_order_remainder = 270 % 10
  print(second_order_remainder)
  second_order_coupon = 'yes'

  def issue_coupon(order_num):
    if order_num % 10 == 0:
      print('Yes')
    else:
      print('No')

  first_order = 269
  second_order = 270
  issue_coupon(first_order)
  issue_coupon(second_order)

#12/15
  string1 = "The wind, "
  string2 = "which had hitherto carried us along with amazing rapidity, "
  string3 = "sank at sunset to a light breeze; "
  string4 = "the soft air just ruffled the water and "
  string5 = "caused a pleasant motion among the trees as we approached the shore, "
  string6 = "from which it wafted the most delightful scent of flowers and hay."

  # Define message below:
  message = string1 + string2 + string3 + string4 + string5 +string6
  print(message)

#13/15
  total_price = 0

  new_sneakers = 50.00

  total_price += new_sneakers

  nice_sweater = 39.00
  fun_books = 20.00
  # Update total_price here:
  total_price += nice_sweater
  total_price += fun_books

  print("The total price is", total_price)

#14/15
  # Assign the string here
  to_you = """
    Stranger, if you passing meet me and desire to speak to me, why should you not speak to me?
    And why should I not speak to you?
  """
  print(to_you)

#15/15
  my_age = 30
  half_my_age = my_age / 5
  greeting = 'Hello, World!'
  name = 'Will'
  greeting_with_name = greeting + ' My name is ' + name + '.'
  print(greeting_with_name)