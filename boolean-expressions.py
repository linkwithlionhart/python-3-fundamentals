#2/12
first_statement = 'Yes'
second_statement = 'Yes'
third_statement = 'No'

#3/12
first_expression = True
second_expression = True
third_expression = False

#4/12
my_baby_bool = 'true'
print(type(my_baby_bool))
my_baby_bool_two = True
print(type(my_baby_bool_two))

#5/12
user_name = "Dave"

if user_name == "Dave":
  print("Get off my computer Dave!")

user_name = "angela_catlady_87"

if user_name == "angela_catlady_87":
  print("I know it is you, Dave! Go away!")

#6/12
x = 20
y = 20

# Write the first if statement here:
if x == y:
  print("These numbers are the same")

credits = 120

# Write the second if statement here:
if credits >= 120:
  print("You have enough credits to graduate!")

#7/12
statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)
# returns false

statement_two = (4 * 2 <= 8) and (7 - 1 == 6)
# returns true

credits = 120
gpa = 3.4

if credits >= 120 and gpa >= 2.0:
  print("You meet the requirements to graduate!")

#8/12
statement_one = (2 - 1 > 3) or (-5 * 2 == -10)
# returns true

statement_two = (9 + 5 <= 15) or (7 != 4 + 3)
#returns true

print(statement_one, statement_two)

credits = 118
gpa = 2.0

if credits >= 120 or gpa >= 2.0:
  print("You have met at least one of the requirements.")

#9/12
statement_one = not (4 + 5 <= 9) # returns false
statement_two = not (8 * 2) != 20 - 4 # returns true
print(statement_one, statement_two)

credits = 120
gpa = 1.8

if not credits >= 120:
  print("You do not have enough credits to graduate.")

if not gpa >= 2.0:
  print("Your GPA is not high enough to graduate.")

if not credits >=120 and not gpa >=2.0:
  print("You do not meet either requirement to graduate!")

#10/12
credits = 120
gpa = 1.9

if (credits >= 120) and (gpa >= 2.0):
  print("You meet the requirements to graduate!")
else: 
  print("You do not meet the requirements to graduate.")


#11/12
grade = 86

if grade >= 90:
  print('A')
elif grade >= 80:
  print('B')
elif grade >= 70:
  print('C')
elif grade >= 60:
  print('D')
else:
  print('F')

#12/12
print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 3

# Write an if statement below:
if planet == 1:
  print('Weight: ' + str(weight*0.91))
elif planet == 2:
  print('Weight: ' + str(weight*0.38))
elif planet == 3:
  print('Weight: ' + str(weight*2.34))
elif planet == 4:
  print('Weight: ' + str(weight*1.06))
elif planet == 5:
  print('Weight: ' + str(weight*0.92))
elif planet == 6:
  print('Weight: ' + str(weight*1.19))
else:
  print('Input the correct planet number.')