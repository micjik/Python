# Exercise 1
# Use Print() to recreate this exact output
# You are allowed to use only one Print()

print("""Your Learning Path:
      \n\t-Python Basics
      \n\t-Data Engineering
      \n\t-AI""")

# Use case 

bread_price = 1.80
butter_price = 1.30

bread_qty = 2
butter_qty = 1

total_bread = bread_price * bread_qty
total_butter = butter_price * butter_price
subtotal = total_bread + total_butter
print("Subtotal:", subtotal)
discount = subtotal * 0.10
print("Discount:", discount)
final_total = subtotal - discount
print("Final Total:", final_total)

# Exercise 2
# Print the following three lines
# Add a variable to make it dynamic
#info@datawithbaraa.com
#support@datawithbaraa.com
#.datawithbaraa.com
my_prefix = "datawithbaraa.com"
print(f"info@{my_prefix}")
print(f"support@{my_prefix}")
print(f"www.{my_prefix}")

# Create 5 variables - each with a different data types
# 1. Your age
# 2. Your height
# 3. Your name
# 4. Are you a student
# 5. Something with no value

# Print the values, data types and the length of each value
my_age = 43
my_height = 6.1
my_name = "Ayodele"
is_student = False
my_profession = None

#print(type(my_age), my_age)
#print(type(my_height), my_height)
#print(type(my_name), my_name, len(my_name))
#print(type(is_student), is_student)
#print(type(my_profession), my_profession)

#Exercise
# Convert the messy phone number into a clean number format with only digits
phone = "+49 (176) 123-4567"
print(phone.replace("+", "00").replace(" ", "").replace("( )", "").replace("-", ""))

#Exercise
#Turn the messy string into a single clean
#summary with name,role, and age
text = "968-Maria, ( Data Engineer );; 27y.."
#clean the string
# name: maria | role: data engineer | age: 27

#EXERCISE
# Generate a random integer between 1 and 100
#and check if the result is even number
