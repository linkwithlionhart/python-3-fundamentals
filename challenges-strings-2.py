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