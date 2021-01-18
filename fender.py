# Codecademy 
# File Reading and Writing Project 
# Hacking the Fender
#
# Student: Scott Balun
# Data: 2021/01/18

# You need to write a program that will read in the usernames and passwords 
# that are stored in a file called "passwords.csv".
the_file = "passwords.csv"
# 
# First import the CSV module, since we’ll be needing it to parse the data.
import csv
import json

#  Create a new list and save it to the variable, compromised_users
compromised_user = []

# Next we need to:
#   1. Open up the file itself. Store it in a file object called, password_file
#   2. Pass the password_file object holder to our CSV reader for parsing
#   3. Save the parsed csv.DictReader object as password_csv
#   4. Iterate through each of the lines in the CSV and save each row into the temp var, password_row
#       - Print out password_row['Username']. 
#   5. Run your code, do you see a list of usernames?
#   6. Remove the print statement. We want to add each username to the list of compromised_users. 
#       - Use the list’s .append() method to add the username to compromised_users instead of printing them.

with open("passwords.csv") as password_file:
    password_csv = csv.DictReader(password_file)

    for line in password_csv:
        password_row = line
        compromised_user.append(password_row['Username'])
        
    print(compromised_user)

# Start a new with block, opening a file called compromised_users.txt. 
#   - Open this file in write-mode, saving the file object as compromised_user_file.
#   - Start a new for loop. Iterate over each of your compromised_users.  
#   - Write the username of each compromised_user in compromised_users to compromised_user_file.

with open("compromised_user.txt", 'w') as compromised_user_file:
    for user in compromised_user:
        compromised_user_file.write(user + '\n')
    
# Import json library
# Open a new JSON file in write-mode called boss_message.json. 
# Save the file object to the variable boss_message.
# Create a Python dictionary object within your with statement that relays a boss message. Call this boss_message_dict.
#   - Give it a "recipient" key with a value "The Boss".
#   - Also give it a "message" key with the value "Mission Success".
#   - Write out boss_message_dict to boss_message using json.dump()

with open("boss_message.json", 'w') as boss_message:
  boss_message_dict = {'recipient': 'The Boss', 'message': 'Mission Success'}
  json.dump(boss_message_dict, boss_message)

# Save the slash null signature as a multiline string to the variable slash_null_sig
slash_null_sig = """
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    | 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( |
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_|
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/"""

# Create a new with block and open "new_passwords.csv" in write-mode. 
# Save the file object to a variable called new_passwords_obj.
# Write slash_null_sig to new_passwords_obj. 
with open("new_passwords.csv", 'w') as new_passwords:
      new_passwords.write(slash_null_sig)

