#1/13 reading files with file.read()
with open('welcome.txt') as text_file:
  text_data = text_file.read()

print(text_data)

#2/13 iterate through lines with file.readlines()
with open('how_many_lines.txt') as lines_doc:
  for line in lines_doc.readlines():
    print(line)

#3/13 reading a line with file.readline()
with open('just_the_first.txt') as first_line_doc:
  first_line = first_line_doc.readline()

  print(first_line)

#4/13 writing a file with open('file.txt', 'w) and file.write('sample')
with open('bad_bands.txt', 'w') as bad_bands_doc:
bad_bands_doc.write('The Beatles')

#5/13 appending to a file with open('file.txt', 'a') and file.write('\n')
with open('cool_dogs.txt', 'a') as cool_dogs_file: 
  cool_dogs_file.write('Air Buddy\n')

#6/13 'with' is a context manager intended to handle outdated sequence: file.open(), file.write(), file.close()
with open('fun_file.txt') as close_this_file:
  setup = close_this_file.readline()
  punchline = close_this_file.readline()

print(setup)
print(punchline)

#7/13 What is a CSV file?