#1/9 key: value pairs
sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

print(sensors)

#2/9 mapping
translations = {
  "mountain": "orod",
  "bread": "bass",
  "friend": "mellon",
  "horse": "roch"
}

#3/9 unhashable types: list and disctionaries
# children = {["Johannes", "Rosmarie", "Eleonore"]: "von Trapp", ["Sonny", "Fredo", "Michael"]: "Corleone"}

children = {
  "von Trapp": ["Johannes", "Rosmarie", "Eleonore"],
  "Corleone": ["Sonny", "Fredo", "Michael"]
}

#4/9 empty dictionary
my_empty_dictionary = {}

#5/9 add a key
animals_in_zoo = {
  "zebras": 8,
  "monkeys": 12,
  "dinosaurs": 0
}

print()

#6/9 add multiple keys with .update()
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}

user_ids.update({
  "theLooper": 138475,
  "stringQueen": 85739
})

print(user_ids)

#7/9 overwrite values
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners["Supporting Actress"] = "Viola Davis"
oscar_winners["Best Picture"] = "Moonlight"

#8/9 dict comprehensions with zip()
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {
  key:value for key, value in zipped_drinks
}
print(drinks_to_caffeine)

#9/9 review
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {
  key:value for key, value in zip(songs, playcounts)
}
print(plays)
plays.update({"Purple Haze": 1})
plays.update({"Respect": 94})
library = {
  "The Best Songs": plays,
  "Sunday Feelings": {}
}
print(library)




