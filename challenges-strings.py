# 1/12
favorite_word = "sushi"
print(favorite_word)

# 2/12 strings are lists of characters
my_name = 'Will'
first_initial = my_name[0]
print(first_initial)

# 3/12 slicing string lists
first_name = "Rodrigo"
last_name = "Villanueva"

new_account = last_name[:5]
print(new_account)

temp_password = last_name[2:6]
print(temp_password)

# 4/12 concatenating strings
first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):
  concat_name = first_name[:3] + last_name[:3]
  return concat_name

new_account = account_generator(first_name, last_name)
print(new_account)

# 5/12 len() of string
first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name):
  concat_name = first_name[len(first_name)-3:] + last_name[len(last_name)-3:]
  return concat_name

temp_password = password_generator(first_name, last_name)
print(temp_password)

# 6/12 negative slices
company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

second_to_last = company_motto[-2]
final_word = company_motto[-4:]
print(second_to_last, final_word)

# 7/12 strings are immutable (property: mutability)
first_name = "Bob"
last_name = "Daily"

fixed_first_name = "R" + first_name[-2:]
print(fixed_first_name)

# 8/12 escape chars '\'
password = "theycallme"crazy"91"
password = "theycallme\"crazy\"91"

# 9/12 iterating through strings
def get_length(string):
  length = 0
  for i in string:
    length += 1
  return length

# 10/12 strings and conditionals
def letter_check(word, letter):
  switch = False
  for char in word:
    print(char)
    if char == letter:
      switch = True
      break
  return switch

letter_check("strawberry", "a")

# 11/12 strings and conditionals
def contains(big_string, little_string):
  if little_string in big_string:
    return True
  else: 
    return False
  
def contains(big_string, little_string):
  if little_string in big_string:
    return True
  else: 
    return False

def common_letters(string_one, string_two):
  matches = []
  for char in string_one:
    if char in string_two and char not in matches:
      matches.append(char)
  return matches

# 12/12
def username_generator(first_name, last_name):
  user_name = first_name[:3] + last_name[:4]
  return user_name

print(username_generator('Abe', 'Simpson'))

# def password_generator(user_name):
#   password = user_name[-1] + user_name[:-1]
#   return password

def password_generator(user_name):
  password = ''
  for i in range(0, len(user_name)):
    password += user_name[i-1]
  return password

print(password_generator(username_generator('Abe', 'Simpson')))
