# Why is handling string data important?
#Text is everywhere FileName, user input, web data
# Types
name = "Ayodele"
print(type(name))
age = 24
print(type(age))
print("Your age is :" + str(age))
age = age + 5
age = str(age)
print(type(age))

# String function Math
password = "123a"
print(len(password))

if(len(password) < 8):
    print("Your password is too short!")

text = """
Python is easy to learn
Python is powerful
Many people love python
"""
print(text.count("python"))

# Data Transformations
price = "1234,56"
price.replace(",", ".")
phone = "176-1234-56"
phone.replace("-", "/")

price = "$1,299.99"
print(price.replace("$", "").replace(",", ""))

first_name = "Michael"
last_name = "Adetayo"
full_name = first_name + " " + last_name
print(full_name)

folder = "c:/users/micjik/"
file = "report.csv"
full_path = folder + file
print(full_path)

name = "sam"
age = 34
is_student = False
print(f"My name is {name} I am {age} years old, and my student status is {is_student}")

#Split
stamp = "2026-09-20 14:30"
print(stamp.split(" "))
stamp = "2026-09-20"
print(stamp.split("-"))

csv_file = "1234,max,USA,1970-10-05,M"
print(csv_file.split(","))

#string operator(*)
print("ha" * 3)
print("====================================")
#instead
print("=" * 30)

#Extraction
# python see any string as a sequence of characters
#slicing [start:end] note that the end is not included
#open-ended slicing [1:]
#[start:End:Step]
#example
#extract the first character
text = "python"
print(text[-6])
#extract the last character
print(text[-1])
date = "2026-09-20"
#Extract only year
print(date[0:4])
date[:4]

#Extract the Month
print(date[5:7])

#Extract the day
print(date[-2:])
#OR
print(date[8: ])

# White spaces Cleaning
# clean white spaces
text = " Engineering".lstrip()

text = "Engineering ".rstrip()

text = " Engineering ".strip()

text = "Data Engineering".strip()

text = "###ABC###".strip("#")

text = " Engineering"
print(len(text))
print(len(text.strip()))

nr_of_spaces = len(text) - len(text.strip())
is_clean = len(text) == len(text.strip())

print(len(text) - len(text.strip()))
print(len(text) == len(text.strip()))

#Case Conversions
text = "python programming"
print(text.lower())
print(text.upper())
search = "Email".lower().strip()
data = "email".lower().strip()
print(search == data)

#Search
#startswith
#endswith
#in
#find
phone = "+49-176-12345"
print(phone.startswith("+49"))

email = "micjik50@gmail.com"
print(email.endswith("gmail.com"))

print("@" in email)

file = "data_backup.csv"
print(file.endswith(".csv"))

url = "https://api.company.com/v1/data"
print("//api" in url)

phone1 = "+48-176-12345"
phone2 = "48-654-16548"
phone3 = "0048-654-16548"

print(phone1[4:])
print(phone1[phone1.find("-")+1:])
print(phone2[phone2.find("-")+1:])

print(phone1.find("-"))

# string validation
#alpha to check if it has only letters
country = "USA"
print(country.isalpha())

phone = "01761234587"
print(phone.isnumeric())

phone = 3.19
# this will not work for isnumeric because is a float




