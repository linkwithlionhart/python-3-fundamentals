# Tenth Power
  # Write your tenth_power function here:

  def tenth_power(num):
    return num ** 10

  # Uncomment these function calls to test your tenth_power function:
  print(tenth_power(1))
  # 1 to the 10th power is 1
  print(tenth_power(0))
  # 0 to the 10th power is 0
  print(tenth_power(2))
  # 2 to the 10th power is 1024

# Square Root
  # Write your square_root function here:
  def square_root(num):
    return num ** 0.5

  # Uncomment these function calls to test your square_root function:
  print(square_root(16))
  # should print 4
  print(square_root(100))
  # should print 10

# Win Percentage
  # Write your win_percentage function here:
  def win_percentage(wins, losses):
    total_games = wins + losses
    win_ratio = wins/total_games
    return win_ratio*100

  # Uncomment these function calls to test your win_percentage function:
  print(win_percentage(5, 5))
  # should print 50
  print(win_percentage(10, 0))
  # should print 100

# Average
  # Write your average function here:
  def average(num1, num2):
    avg = (num1+num2)/2
    return avg

  # Uncomment these function calls to test your average function:
  print(average(1, 100))
  # The average of 1 and 100 is 50.5
  print(average(1, -1))
  # The average of 1 and -1 is 0

# Remainder
  # Write your remainder function here:
  def remainder(num1, num2):
    twice = num1*2
    half = num2/2
    remain = twice % half
    return remain

  # Uncomment these function calls to test your remainder function:
  print(remainder(15, 14))
  # should print 2
  print(remainder(9, 6))
  # should print 0

# First Three Multiples
  # Write your first_three_multiples function here
  def first_three_multiples(num):
    print(1*num)
    print(2*num)
    print(3*num)
    return 3*num

  # Uncomment these function calls to test your first_three_multiples function:
  first_three_multiples(10)
  # should print 10, 20, 30, and return 30
  first_three_multiples(0)
  # should print 0, 0, 0, and return 0

# Tip
  # Write your tip function here:
  def tip(total, percentage):
    tip = total * (percentage/100)
    return tip
    
  # Uncomment these function calls to test your tip function:
  print(tip(10, 25))
  # should print 2.5
  print(tip(0, 100))
  # should print 0.0

# Bond, James Bond
  # Write your introduction function here:
  def introduction(first_name, last_name):
    return f'{last_name}, {first_name} {last_name}'

  # Uncomment these function calls to test your introduction function:
  print(introduction("James", "Bond"))
  # should print Bond, James Bond
  print(introduction("Maya", "Angelou"))
  # should print Angelou, Maya Angelou

# Dog Years
  # Write your dog_years function here:
  def dog_years(name, age):
    age = age*7
    return f"{name}, you are {age} years old in dog years"

  # Uncomment these function calls to test your dog_years function:
  print(dog_years("Lola", 16))
  # should print "Lola, you are 112 years old in dog years"
  print(dog_years("Baby", 0))
  # should print "Baby, you are 0 years old in dog years"

# All Operations
  # Write your lots_of_math function here:
  def lots_of_math(a,b,c,d):
    print(a+b)
    print(c-d)
    print((a+b)*(c-d))
    return ((a+b)*(c-d)) % a

  # Uncomment these function calls to test your lots_of_math function:
  print(lots_of_math(1, 2, 3, 4))
  # should print 3, -1, -3, 0
  print(lots_of_math(1, 1, 1, 1))
  # should print 2, 0, 0, 0