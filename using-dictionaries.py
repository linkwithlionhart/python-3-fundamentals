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