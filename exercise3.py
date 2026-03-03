# print the 7 times tsble from 1 to 10 using a for loop
x = 7
for i in range(1, 11):
    print(x * i)

# print a left aligned pyramid of stars with 6 rows using a for loop
y = x
for i in range(6):
    print(y * i)

# Advanced Loop using the break statement
names = ["John", "Maria", "", "Kumar"]
for name in names:
    if name == "":
        print("Empty value detected")
        break
    
    print(name)

# Advanced Loop using the continue statement
names = ["John", "Maria", "", "Kumar"]
for name in names:
    if name == "":
        print("Empty value detected")
        continue
    
    print(name)

# Advanced Loop using the Pass statement
names = ["John", "Maria", "", "Kumar"]
for name in names:
    if name == "":
        print("Empty value detected")
        pass #todo:Handle empty value
    
    print(name)

# Use case Scenario using Break and Continue Statement
# Loop through a list of days and print only the working days, skipping the weekends
days = ['mon', 'tues', 'wed', 'thurs', 'fri', 'sat', 'sun']

for day in days:
    if day in ['sat', 'sun']:
        print("It is not a working day")
        break
    print(f'it is a working day: {day}')

# Scan emails to block unsafe data from entering the system
emails = [
    'data@gmail.com',
    'baraa@outlook.com',
    'DROP TABLE USERS;',
    'maria@gmail.com'
]
for email in emails:
    if ';' in email:
        print('SQL Injection: Hacker Attack')
        break
    print(f'processing Email: {email}')

## Break Critical Risk
# cost
# security

## Continue Medium risk
# bad rows
#empty file/Data
# skip special cases

## Pass placeholder
# do nothing

# Use else with loops only when there's a break
# check for even numbers
items = [1, 3, 4, 7]
for i in items:
    if i % 2 == 0:
        print("Even Nr. Found", i)
        break
else:
    print("All numbers are odd")

# Validate and search
names = ['kamara', 'Tuba', None, 'Mounika']

for name in names:
    if name is None:
        print('Found a missing name')
        break
else:
    print("All names are valid")

# check all files are csv
files = ['data.csv', 'report.pdf', 'report2.csv']

for file in files:
    if not file.endswith('.csv'):
        print(f'{file} is not a csv')
        break
else:
    print('All files are CSV')