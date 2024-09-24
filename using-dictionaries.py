#1/9 
"""
Use a key to get a value from a dictionary
Check for existence of keys
Iterate through keys and values in dictionaries
"""

#2/9 access keys
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

print(zodiac_elements["earth"])
print(zodiac_elements["fire"])

#3/9 invalid keys
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"], "energy": "Not a Zodiac element"}

# print(zodiac_elements["energy"])
# KeyError: 'energy'

if 'energy' in zodiac_elements:
  print(zodiac_elements['energy'])

#4/9 safely access key with object.get(key, DNE-value)
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get('teraCoder', 100000)
print(tc_id)

stack_id = user_ids.get('superStackSmash', 100000)
print(stack_id)
# returns default value of 100000 because it DNE

#5/9 delete a key with object.pop(key, DNE-value)
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20
print(health_points)

health_points += available_items["stamina grains"]
available_items.pop("stamina grains", 0)
print(health_points, available_items)

health_points += available_items.pop("power stew", 0)
print(health_points, available_items)

health_points += available_items.pop("mystic bread", 0)
print(health_points, available_items)

#6/9 get all keys with object.keys() - returns immutable object
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()
lessons = num_exercises.keys()
print(list(user_ids))
print(list(num_exercises))
print(users)
print(lessons)

for user in users:
  print(user)

for lesson in lessons:
  print(lesson)

#7/9 get all values with object.values()
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0
for exercise in num_exercises.values():
  total_exercises += exercise

print(total_exercises)

#8/9 get all items with object.items()
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for occupation, value in pct_women_in_occupation.items():
  print(f'Women make up {value} percent of {occupation}s.')

#9/9 review
tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread = {}
spread["past"] = tarot.pop(13)
spread["present"] = tarot.pop(22)
spread["future"] = tarot.pop(10)
print(spread)

for key, value in spread.items():
  print(f'Your {key} is the {value} card.')