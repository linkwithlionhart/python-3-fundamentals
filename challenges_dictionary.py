#1 Sum Values
"""
Define the function to accept one parameter for our dictionary
Create a variable to keep track of our sum
Loop through every value in the dictionary
Inside the loop, add each value to the sum
Return the sum
"""
# Write your sum_values function here:
def sum_values(my_dictionary):
  total = 0
  for value in my_dictionary.values():
    total += value
  return total

# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6

#2 Even Keys
"""
Define the function to accept one parameter for our dictionary
Create a variable to keep track of our sum
Loop through every key in the dictionary
Inside the loop, if the key is even, add the value from the even key
After the loop, return the sum
"""
# Write your sum_even_keys function here:
def sum_even_keys(my_dictionary):
  total = 0
  for key in my_dictionary:
    if key % 2 == 0:
      total += my_dictionary[key]
  return total

# Uncomment these function calls to test your  function:
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6

#3 Add Ten
"""
Define the function to accept one parameter for our dictionary
Loop through every key in the dictionary
Retrieve the value using the key and add 10 to it. Make sure to re-save the new value to the original key.
After the loop, return the modified dictionary
"""
# Write your add_ten function here:

def add_ten(my_dictionary):
  for key in my_dictionary:
    my_dictionary[key] += 10
  return my_dictionary

# Uncomment these function calls to test your  function:
print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}

#4 Values That Are Keys
"""
Define the function to accept one parameter for our dictionary
Create an empty list to hold the values we find
Loop through every value in the dictionary
Inside the loop, test if the current value is a key in the dictionary. If it is then append it to the list of values we found
After the loop, return the list of values which are also keys
"""
# Write your values_that_are_keys function here:
def values_that_are_keys(my_dictionary):
  value_keys = []
  for value in my_dictionary.values():
    if value in my_dictionary.keys():
      value_keys.append(value)
  return value_keys


# Uncomment these function calls to test your  function:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]

#5 Largest Value
"""
Define the function to accept one parameter for our dictionary
Initialize the starting key to a very low number
Initialize the starting value to a very low number
Iterate through the dictionary’s key/value pairs.
Inside the loop, if the current value is larger than the current largest value, replace the largest key and largest value with the current ones you are looking at
Once you are done iterating through all key/value pairs, return the key which has the largest value
"""
# Write your max_key function here:
def max_key(my_dictionary):
  val_list = [value for value in my_dictionary.values()]
  val_list.sort(reverse=True)
  for key, value in my_dictionary.items():
    if value == val_list[0]:
      return key

# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"

# Solution
def max_key(my_dictionary):
  largest_key = float("-inf")
  largest_value = float("-inf")
  for key, value in my_dictionary.items():
    if value > largest_value:
      largest_value = value
      largest_key = key
  return largest_key

#6 Word Length Dict
"""
Define the function to accept one parameter for our list of strings
Create a new empty dictionary
Loop through every string in the list of strings
Inside the loop, add the string as a key and the length of the string as the value to the dictionary
After the loop, return the new dictionary
"""
# Write your word_length_dictionary function here:
# Using dictionary.update() method
"""def word_length_dictionary(words):
  new_dict = {}
  for word in words:
    new_dict.update({word:len(word)})
  return new_dict"""

# Using 
def word_length_dictionary(words):
  word_lengths = {}
  for word in words:
    word_lengths[word] = len(word)
  return word_lengths

# Uncomment these function calls to test your  function:
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}

#7 Frequency Count
"""
Define the function to accept one parameter for our list of strings
Create a new empty dictionary
Loop through every string in the list of strings
Inside the loop, if the string is NOT already in our dictionary, store the string as a key with a value of 0 in our dictionary. Otherwise, if the string is already in our dictionary, increment the value by 1.
After the loop, return the new dictionary
"""
# Write your frequency_dictionary function here:

def frequency_dictionary(words):
  word_freq = {}
  for word in words:
    if word not in word_freq:
      word_freq[word] = 1
    else: word_freq[word] += 1
  return word_freq

# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}

# Solution
def frequency_dictionary(words):
  freqs = {}
  for word in words:
    if word not in freqs:
      freqs[word] = 0
    freqs[word] += 1
  return freqs

#8 Unique Values
"""
Define the function to accept one parameter for our dictionary
Create a new empty list
Loop through every value in our dictionary
Inside the loop, if the value is not already in our list, append the value to our list
After the loop, return the length of our list  
"""
# Write your unique_values function here:
def unique_values(my_dictionary):
  unique = []
  for value in my_dictionary.values():
    if value not in unique:
      unique.append(value)
  return len(unique)

# Uncomment these function calls to test your  function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1

#9 Count First Letter
"""
Define the function to accept one parameter for our dictionary
Create a new empty dictionary called letters
Loop through every key in our names dictionary
Inside the loop, get the first letter of the last name we are looking at. If the first letter is not in our letter dictionary, add it as a key and set the value to the number of people that have that last name. Otherwise, if the first letter is already in our letter dictionary, increment the value stored with that key by the number of people that have that last name
After the loop, return the letters dictionary
"""
# Write your count_first_letter function here:
def count_first_letter(names):
  counts = {}
  for key, value in names.items():
    if key[:1] not in counts:
      counts[key[:1]] = 0
    counts[key[:1]] += len(value)
  return counts

# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}

# Solution
def count_first_letter(names):
  letters = {}
  for key in names:
    first_letter = key[0]
    if first_letter not in letters:
      letters[first_letter] = 0
    letters[first_letter] += len(names[key])
  return letters