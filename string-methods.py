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

#6/13 ' '.join(list)
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = ' '.join(reapers_line_one_words)
print(reapers_line_one)

#7/13 '\n'.join(list)
winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = '\n'.join(winter_trees_lines)

print(winter_trees_full)

#8/13 string.strip()
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = []
for line in love_maybe_lines:
  love_maybe_lines_stripped.append(line.strip())

print(love_maybe_lines_stripped)

love_maybe_full = '\n'.join(love_maybe_lines_stripped)
print(love_maybe_full)

#9/13 string.replace(replacee, replacer)
toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""
toomer_bio_fixed = toomer_bio.replace('Tomer', 'Toomer')
print(toomer_bio_fixed)

#10/13 string.find('target') returns the index value of the first match it finds
god_wills_it_line_one = "The very earth will disown you"

disown_placement = god_wills_it_line_one.find('disown')
print(disown_placement)

#11/13 string{}.format(variable1, variable2, etc.)
def poem_title_card(title, poet):
  return 'The poem "{}" is written by {}.'.format(title, poet)

print(poem_title_card("I Hear America Singing", "Walt Whitman"))

#12/13
def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
  return poem_desc

my_beard_description = poem_description(
  author = "Shel Silverstein",
  title = "My Beard",
  original_work = "Where the Sidewalk Ends",
  publishing_date = "1974"
)

print(my_beard_description)

#13/13 review
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
# print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(',')
# print(highlighted_poems_list)

highlighted_poems_stripped = []
for poem in highlighted_poems_list:
  highlighted_poems_stripped.append(poem.strip())
# print(highlighted_poems_stripped)

highlighted_poems_details = []
for poem in highlighted_poems_stripped:
  highlighted_poems_details.append(poem.split(':'))
# print(highlighted_poems_details)

titles = []
poets = []
dates = []

for this_list in highlighted_poems_details:
  titles.append(this_list[0])
  poets.append(this_list[1])
  dates.append(this_list[2])
# print(titles, poets, dates)

for this_list in highlighted_poems_details:
  print('The poem, {TITLE}, was published by {POET} in {DATE}.'.format(TITLE=this_list[0], POET=this_list[1], DATE=this_list[2]))

for i in range(len(titles)):
  print('The poem, {TITLE}, was published by {POET} in {DATE}.'.format(TITLE=titles[i], POET=poets[i], DATE=dates[i]))