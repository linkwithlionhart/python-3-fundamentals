# Build Point Dictionary
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# print(len(letters), len(points))
letters_to_points = {key:value for key, value in zip(letters, points)}

letters_to_points[" "] = 0
print(letters_to_points)

# Score a word
def score_word(word):
  check_word = word.upper()
  point_total = 0
  for letter in check_word:
    if letter in letters_to_points:
      point_total += letters_to_points[letter]
  print(point_total)
  return point_total

brownie_points = score_word('BROWNIE')

# Score a game
player_to_words = {
  "BLUE": ["EARTH", "ERASER", "ZAP"],
  "TENNIS": ["EYES", "BELLY", "COMA"],
  "EXIT": ["MACHINE", "HUSKY", "PERIOD"]
}

player_to_points = {}
for player, words in player_to_words.items():
  print(player, words)
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points
  print(player_points)
print(player_to_points)

# Ideas for Further Practice!

