#1 Count letters
"""
Define the function to accept one parameter — the word whose letters we are counting
Create a counter to keep track of unique letters
Loop through every letter in our alphabet string. If the current letter was found in our word, increase our count
Return the count after looping through all letters.
"""
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters(word):
  unique_list = []
  for letter in word:
    if letter in letters and letter not in unique_list:
      unique_list.append(letter)
  return len(unique_list)

# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4

#2 Count X
"""
Define the function to accept two parameters. word for the input string and x for the single character
Create a counter to keep track of the occurrences
Loop through every letter in the string. If the current letter is equal to the input letter, increase our counter
Return the counter after looping through the entire string.
"""
# Write your count_char_x function here:
def count_char_x(word, x):
  count = 0
  for letter in word:
    if letter == x:
      count += 1
  return count

# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1

#3 Count Multi X
"""
Define the function to accept two parameters. word for the input string and x for the second string we are searching for
Split the string into substrings based on the second input parameter
Count the number of instances the substring appeared in the first input string based on the split string
Return the result
"""
# Write your count_multi_char_x function here:
def count_multi_char_x(word, x):
  return len(word.split(x)) - 1

# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1

#4 Substring Between
"""
Define the function to accept three parameters, one string and two characters
find the starting index of our substring using the second input parameter
find the ending index of our substring using the third input parameter
If neither of the indices are -1, return the portion of the first input parameter string between the starting and ending indices (not including the starting and ending index)
If either of the indices are -1, that means the start or end of the substring didn’t exist in our string. Return the original string in this case.
"""
# Write your substring_between_letters function here:

def substring_between_letters(word, start, end):
  start_index = word.find(start)
  end_index = word.find(end)
  # print(start_index, end_index)
  if start_index == -1 or end_index == -1:
    return word
  else:
    return word[start_index+1:end_index]

# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"

#5 X Length
"""
Define the function to accept two parameters, one string, and one number
Split up the sentence into an array of words
Loop through the words. If the length of any of the words is less than the provided number return False
If we made it through the loop without returning False then return True
"""
# Write your x_length_words function here:
def x_length_words(sentence, x):
  for word in sentence.split():
    if len(word) < x:
      return False
  return True

# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True

#6 Check Name
"""
Define the function to accept two parameters, one string for the sentence and one string for the name
Convert all of the strings to the same case so we don’t have to worry about differences in capitalization
Check if the name is within the sentence. If so, then return True. Otherwise, return False
"""
# Write your check_for_name function here:

"""def check_for_name(sentence, name):
  lower_sentence = sentence.lower().split()
  lower_name = name.lower()
  if lower_name in lower_sentence:
    return True
  return False"""

def check_for_name(sentence, name):
  return name.lower() in sentence.lower()

# Uncomment these function calls to test your  function:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False

#7 Every Other Letter
"""
Define the function to accept one parameter for the string
Create a new empty string to hold every other letter from the input string
Loop through the input string while incrementing by two every time
Inside the loop, append the character at the current location to the new string we initialized earlier
Return the new string
"""
# Write your every_other_letter function here:

def every_other_letter(word):
  other_string = ""
  for i in range(0, len(word), 2):
    other_string += word[i]
  return other_string

# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print  

#8 Reverse
# Write your reverse_string function here:
def reverse_string(word):
  rev_word = ""
  for i in range(len(word)-1, -1, -1):
    rev_word += word[i]
  return rev_word

# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print

#9 Make Spoonerism
"""
Define the function to accept two parameters for our two words
Get the first character of the first word and the first character of the second word
Get the remaining characters of the first word and the remaining characters of the second word.
Append the first character of the second word to the remaining character of the first word
Append a space character
Append the first character of the first word to the remaining characters of the second word.
Return the result
"""
# Write your make_spoonerism function here:

def make_spoonerism(word1, word2):
  first_word = word2[0] + word1[1:]
  second_word = word1[0] + word2[1:]
  return f"{first_word} {second_word}"

# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a

# Solution
def make_spoonerism(word1, word2):
  return word2[0]+word1[1:]+" "+word1[0]+word2[1:]

#10 Add Exclamation
"""
Define the function to accept one parameter for our string
Loop while the length of our input string is less than 20
Inside the loop, append an exclamation mark
Once done, return the result
"""
# Write your add_exclamation function here:

def add_exclamation(word):
  count = len(word)
  mod_word = word
  while(count < 20):
    mod_word += "!"
    count = len(mod_word)
  else:
    return mod_word

# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn

# Solution
def add_exclamation(word):
  while(len(word) < 20):
    word += "!"
  return word