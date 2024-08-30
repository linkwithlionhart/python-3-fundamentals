#2/13
  # Write 10 print() statements below! 
  print("This can be so much easier with loops!")
  print("This can be so much easier with loops!")
  print("This can be so much easier with loops!")
  print("This can be so much easier with loops!")  
  print("This can be so much easier with loops!")
  print("This can be so much easier with loops!")  
  print("This can be so much easier with loops!")
  print("This can be so much easier with loops!")  
  print("This can be so much easier with loops!")
  print("This can be so much easier with loops!")    

#3/13
  board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

  sport_games = ["football", "hockey", "baseball", "cricket"]

  for game in board_games:
    print(game)

  for game in sport_games:
    print(game)

#4/13 For Loops: Using Range
  promise = "I will finish the python loops module!"

  for num in range(5):
    print(promise)

#5/13 While Loops: Introduction
  # while Loop Walkthrough
  count = 0
  print("Starting While Loop")
  while count <= 3:
    # Loop Body
    # Print if the condition is still true
    print("Loop Iteration - count <= 3 is still true")
    # Print the current value of count 
    print("Count is currently " + str(count))
    # Increment count
    count += 1
    print(" ----- ")
  print("While Loop ended")

  # Your code below: 
  countdown = 10
  while countdown >= 0:
    print(countdown)
    countdown -= 1

  print("We have liftoff!")

#6/13 While Loops: Lists
  python_topics = ["variables", "control flow", "loops", "modules", "classes"]

  #Your code below: 
  length = len(python_topics)
  index = 0 
  while index < length:
    print(f"I am learning about {python_topics[index]}")
    index += 1

#7/13 Infinite Loops
  students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
  students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

  for student in students_period_A:
    students_period_B.append(student)
    print(student)

#8/13 Loop Control: Break
  dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
  dog_breed_I_want = "dalmatian"

  for dog_breed in dog_breeds_available_for_adoption:
    print(dog_breed)
    if dog_breed == dog_breed_I_want:
      print("They have the dog I want!")
      break

#9/13 Loop Control: Continue
  ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

  for age in ages:
    if age < 21:
      continue
    print(age)

#10/13 Nested Loops
  sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

  scoops_sold = 0
  for location in sales_data:
    print(location)
    for sales in location:
      scoops_sold += sales

  print(scoops_sold)

  """
  Accurate naming will help with understanding targeted instances and collections.
  """

#11/13 List Comprehensions: Introduction
  grades = [90, 88, 62, 76, 74, 89, 48, 57]
  scaled_grades = [num + 10 for num in grades]
  print(scaled_grades)

#12/13 List Comprehensions: Conditionals
  heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
  can_ride_coaster = [height for height in heights if height > 161]
  print(can_ride_coaster)

#13/13 Review
# Your code below:
  single_digits = range(0, 10)
  squares = []

  for digit in single_digits:
    print(digit)
    squares.append(digit**2)

  print(squares)

  cubes = [digit ** 3 for digit in single_digits]
  print(cubes)