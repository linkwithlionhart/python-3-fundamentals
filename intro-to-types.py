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
Instance variables aren’t shared by all instances of a class 
— they are variables that are specific to the object they are attached to.
"""
class Store:
  pass

alternative_rocks = Store()
isabelles_ices = Store()

# instance attributes
alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"

#10/14 attribute functions