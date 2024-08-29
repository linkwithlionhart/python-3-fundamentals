#2/12 list.insert()
  front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
  print(front_display_list)

  # Your code below: 
  front_display_list.insert(0, "Pineapple")
  print(front_display_list)

#3/12 list.pop()
  data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
  print(data_science_topics)

  # Your code below: 
  data_science_topics.pop()
  print(data_science_topics)
  data_science_topics.pop(3)
  print(data_science_topics)

#4/12 list(range(start, stop, step))
  # Your code below: 

  number_list = range(0,9)
  print(type(number_list))
  print(list(number_list))

  zero_to_seven = range(0,8)
  print(list(zero_to_seven))

#5/12 list(range(start, stop, step))
  # Your code below: 

  range_five_three = range(5, 15, 3)
  range_diff_five = range(0, 40, 5)

#6/12 len()
  long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]

  big_range = range(2, 3000, 100)

  # Your code below: 
  long_list_len = len(long_list)
  print(long_list_len)
  big_range_length = len(big_range)
  print(big_range_length)

#7/12 slicing lists part 1
  suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

  beginning = suitcase[0:2]
  middle = suitcase[2:4]

  # Your code below: 
  print(beginning)
  print(middle)


#8/12 slicing lists part 2
  suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

  # Your code below:
  last_two_elements = suitcase[-2:]
  print(last_two_elements)
  slice_off_last_three = suitcase[:-3]
  print(slice_off_last_three)

#9/12 list.count(value)
  votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

  # Your code below: 
  jake_votes = votes.count('Jake')
  print(jake_votes)

#10/12 list.sort()
  # Checkpoint 1 & 2
  addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]
  addresses.sort()
  print(addresses)

  # Checkpoint 3
  names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
  names.sort()
  print(names)

  # Checkpoint 4 & 5
  cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
  sorted_cities = cities.sort(reverse=True)
  print(sorted_cities)
  # method does not return the values of the sorted list
  print(cities)

#11/12 sorted()
  games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]

  # Your code below:
  games_sorted = sorted(games)
  print(games, games_sorted)

#12/12 review