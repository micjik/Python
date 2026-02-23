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
