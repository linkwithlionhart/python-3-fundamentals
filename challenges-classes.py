#1 Setting up our robot
"""
Create a new class called DriveBot
Set up a basic constructor (no parameters needed)
Initialize three instance variables within our constructor which all default to 0: motor_speed, direction, and sensor_range
"""
# Define the DriveBot class here!
class DriveBot():
  def __init__(self):
    self.motor_speed = 0
    self.direction = 0
    self.sensor_range = 0

robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)

#2 Adding Robot Logic
"""
Define a function within the DriveBot class which accepts two additional parameters: one for a new speed and one for a new direction
Replace the instance variables for speed and direction with the input parameters
Define another function called adjust_sensor which accepts one additional parameter
Replace the instance variable sensor_range with the input parameter
"""
class DriveBot:
    # Add the methods here!
    def control_bot(self, new_speed, new_direction):
      self.motor_speed = new_speed
      self.direction = new_direction
    
    def new_sensor_range(self, sensor_range):
      self.sensor_range = sensor_range

robot_1 = DriveBot()
# Use the methods here!
robot_1.control_bot(10, 180)
robot_1.new_sensor_range(20)

print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)

#3 Enhanced Constructor
"""
Modify the constructor to take three parameters (in addition to self): one for motor_speed, one for direction, and one for sensor_range
For the first parameter, make the default value 0
For the second parameter, make the default value 180
For the third parameter, make the default value 10
Within the constructor, replace the instance variables with the variables from the input parameters
"""
class DriveBot:
    # Update this constructor!
    def __init__(self, motor_speed=0, direction=180, sensor_range=10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
    
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

# Create robot_2 here!
robot_2 = DriveBot(35, 75, 25)

print(robot_2.motor_speed)
print(robot_2.direction)
print(robot_2.sensor_range)

# sensor_range defaults to 10
test_bot_1 = DriveBot(10, 270) 

# direction defaults to 180
test_bot_2 = DriveBot(sensor_range = 20, motor_speed = 45) 

# direction defaults to 180 and sensor_range defaults to 10
test_bot_3 = DriveBot(50) 

# all default values are used
test_bot_4 = DriveBot() 

# no default values are used
test_bot_5 = DriveBot(18, 95, 30)

#4 Controlling Them All
"""
Create a new class variable within the DriveBot class called all_disabled and set it equal to False
Create a new class variable within the DriveBot class called latitude and set it equal to -999999
Create a new class variable within the DriveBot class called longitude and set it equal to -999999
Outside of the class, test the class variables by setting the longitude of all robots to 50.0, the latitude to -50.0 and all_disabled to True
"""
class DriveBot:
  # Create the class variables!
    all_disabled = False
    latitude = -999999
    longitude = -999999

    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
    
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

robot_2 = DriveBot(35, 75, 25)
robot_3 = DriveBot(20, 60, 10)

# Change the latitude, longitude, and all_disabled values for all three robots using only three lines of code!
DriveBot.latitude = -50.0
DriveBot.longitude = 50.0
DriveBot.all_disabled = True

print(robot_1.latitude)
print(robot_2.longitude)
print(robot_3.all_disabled)

#5 Identifying Robots
"""
Create a new class variable in the DriveBot class called robot_count
In the constructor, increment the robot_count by 1
After incrementing the value, assign the value of robot_count to a new instance variable called id.
"""
class DriveBot:
  # Create a counter to keep track of how many robots were created
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0

    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
        # Assign an `id` to the robot when it is constructed by incrementing the counter and assigning the value to `id`
        DriveBot.robot_count += 1
        self.id = DriveBot.robot_count
    
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

robot_2 = DriveBot(35, 75, 25)
robot_3 = DriveBot(20, 60, 10)

print(robot_1.id)
print(robot_2.id)
print(robot_3.id)