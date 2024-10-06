#1/14 find type with type()
print(type(5))
my_dict = {}
print(type(my_dict))
my_list = []
print(type(my_list))

#2/14 initiate class
class Facade:
  pass 

#3/14 instantiate a class
class Facade:
  pass

facade_1 = Facade()

#4/14 return class that object is instance of with type(object)
class Facade:
  pass

facade_1 = Facade()
facade_1_type = type(facade_1)
print(facade_1_type)

#5/14 class variables - you can access all of an object’s class variables with object.variable syntax
class Grade:
  minimum_passing = 65

student = Grade()
print(student.minimum_passing)

#6/14 methods - first argument in a method is always the object that is calling the method. 
# Convention recommends that we name this first argument self.
class Rules:
  def washing_brushes(self):
    return "Point bristles towards the basin while washing your brushes."

cleaning_rule = Rules()
print(cleaning_rule.washing_brushes())

#7/14 methods with arguments
class Circle:
  pi = 3.14
  def area(self, radius):
    return self.pi * radius ** 2

# create an instance
circle = Circle()

pizza_area = circle.area(12/2)
teaching_table_area = circle.area(36/2)
round_room_area = circle.area(11460/2)

print(pizza_area, teaching_table_area, round_room_area)

#8/14 constructors
# Dunder methods (abbr: double-under score): special class methods
class Circle:
  pi = 3.14
  
  # Add constructor here:
  def __init__(self, diameter):
    # pass
    print(f"New circle with diameter: {diameter}")
  
teaching_table = Circle(36)

#9/14 instance variables
"""
We’ve learned so far that a class is a schematic for a data type and an object is an instance of a class, 
but why is there such a strong need to differentiate the two if each object can only have the methods and class variables the class has? 
This is because each instance of a class can hold different kinds of data.

The data held by an object is referred to as an instance variable. 
Instance variables aren’t shared by all instances of a class — they are variables that are specific to the object they are attached to.
"""
class Store:
  pass

alternative_rocks = Store()
isabelles_ices = Store()

# instance attributes
alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"

#10/14 attribute functions 
# if we attempt to access an attribute that is neither classs variable or instance variable of the object Python, it will throw an AttributeError

class NoCustomAttributes:
  pass
attributeless = NoCustomAttributes()
try:
  attributeless.fake_attribute
except AttributeError:
  print("This text gets printed!")
  # prints "This text gets printed!"

# checking for attributes with hasattr(object, "attribute") and getattr(object, "attribute", optional:defaultDNEvalue)
hasattr(attributeless, "fake_attribute")
# returns False
getattr(attributeless, "other_fake_attribute", 800)
# returns 800, the default value

can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in can_we_count_it:
  if hasattr(element, "count"):  
    print(str(type(element)) + " has the count attribute!")
  else: 
    print(str(type(element)) + " does not have the count attribute :(")

#11/14 self
class Circle:
  pi = 3.14
  #class dunder method
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    self.radius = diameter/2
  # reguular class method
  def circumference(self):
    return 2*self.pi*self.radius

medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

#12/14 everything is an object, we can use dir() to check on object's attributes
# print(dir(5))

def this_function_is_an_object(num):
  return "Cheese is {} times better than everything else".format(num)

print(dir(this_function_is_an_object(7)))

#13/14 string representation with dunder method __repre__(self)
class Circle:
  pi = 3.14
  
  def __init__(self, diameter):
    self.radius = diameter / 2
  
  def __repr__(self):
    return f"Circle with radius {self.radius}."

  def area(self):
    return self.pi * self.radius ** 2
  
  def circumference(self):
    return self.pi * 2 * self.radius
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza, teaching_table, round_room)

#14/14 review
# Add a constructor for Student. Have the constructor take in two parameters: a name and a year. Save those two as attributes .name and .year.

class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)
    else:
      pass

class Grade:
  minimum_passing = 65
  def __init__(self, score):
    self.score = score

roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

new_grade = Grade(100)
# print(new_grade.score)

pieter.add_grade(new_grade)
print(pieter.grades[0].score)
