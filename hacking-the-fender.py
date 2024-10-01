"""
The Fender, a notorious computer hacker and general villain of the people, 
has compromised several top-secret passwords including your own. 
Your mission, should you choose to accept it, is threefold. 
You must acquire access to The Fender‘s systems, you must update his "passwords.csv" file to scramble the secret data. 
The last thing you need to do is add the signature of Slash Null, 
a different hacker whose nefarious deeds could be very conveniently halted by The Fender if they viewed Slash Null as a threat.
"""
import csv

compromised_users = []
fields = ["Username", "Password"]
with open('passwords.csv', newline='') as password_file:
  password_csv = csv.DictReader(password_file, delimiter=',')
  for password_row in password_csv:
    print(password_row['Username'])
