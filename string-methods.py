#1/13
"""
list.upper() return uppercase
list.lower() return lowercase
list.split() return title case
"""

#2/13 string.upper(), string.lower(), string.title()
poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()
print(poem_title_fixed)

poem_author_fixed = poem_author.upper()
print(poem_author_fixed)

#3/13 string.split() into substrings
line_one = "The sky has given over"
line_one_words = line_one.split()
print(line_one_words)

#4/13 string.split(delimiter) into substrings
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(',')
print(author_names)

author_last_names = []
for full_name in author_names:
  author_last_names.append(full_name.split()[-1]) # extraction is chained to the split method
print(author_last_names)

#5/13 escape sequences using \n for newline or \t for horizontal tab
spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split('\n')
print(spring_storm_lines)

#6/13 


#7/13


#8/13


#9/13


#10/13


#11/13


#12/13


#13/13

