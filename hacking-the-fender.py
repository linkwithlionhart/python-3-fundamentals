import csv

# Reading in the Passwords
compromised_users = []
# fields = ["Username", "Password"]
with open('passwords.csv', newline='') as password_file:
  password_csv = csv.DictReader(password_file, delimiter=',')
  for password_row in password_csv:
    # print(password_row['Username'])
    compromised_users.append(password_row['Username'])

print(compromised_users)

with open('compromised_users.txt', 'w') as compromised_user_file:
  for user in compromised_users:
    compromised_user_file.write(user+'\n')

# Notifying the Boss
import json

with open('boss_message.json', 'w') as boss_message:
  boss_message_dict = {
    "recipient": "The Boss",
    "message": "The Mission Success"
  }
  json.dump(boss_message_dict, boss_message)

# Scrambling the Password
