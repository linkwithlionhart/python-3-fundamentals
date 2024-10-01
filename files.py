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
with open('logger.csv') as log_csv_file:
  log_csv = log_csv_file.read()

print(log_csv)

#8/13 reading a file with csv module, DictReader method, and newline='' arg
import csv 

with open('cool_csv.csv', newline='') as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)
  for row in cool_csv_dict:
    print(row['Cool Fact'])

#9/13 reading Different Types of CSV Files with csv.DictReader(file, delimiter='symbol')
import csv 

isbn_list = []
with open('books.csv', newline='') as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter='@')
  for row in books_reader:
    isbn_list.append(row['ISBN'])
print(isbn_list)

#10/13 writing a CSV File with object.writeheader() and object.writerow()
access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']

import csv

with open('logger.csv', 'w') as logger_csv:
  log_writer = csv.DictWriter(logger_csv, fieldnames=fields)
  print(log_writer)
  
  log_writer.writeheader()
  for item in access_log:
    log_writer.writerow(item)

#11/13 reading a JSON file by parsing purchase_json using json.load()
import json

with open('message.json') as message_json:
  message = json.load(message_json)

print(message['text'])
print(message['secret text'])

#12/13 writing a JSON file with json.dump(turn_to_json, json_file)
data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]

import json 

with open('data.json', 'w') as data_json:
  json.dump(data_payload, data_json)

#13/13 review
"""
Open up file objects using open() and with.
Read a file’s full contents using Python’s .read() method.
Read a file line-by-line using .readline() and .readlines()
Create new files by opening them in write-mode.
Append to a file non-destructively by opening a file in append-mode.
Apply all of the above to different types of data-carrying files including CSV and JSON!
"""

