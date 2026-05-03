# what are function
# A small reusable code or set of instruction that does a 
# specific task. Instead of using a particular set of code repeatedly, use put them in a function
# code Modularity - divide it into smaller pieces.
# types of function
# Built in function => comes with python itself
# standard library = written by python team, you need to import them in order to use them
# External Library => written by community, you need to install, import and use them
# User-Defined Functions => written by you.

# Golden rules Before writing new code, Always check if it already exists
# 1. check the built-in functions safe and easy
# 2. check the libraries
# 3. check with your team -> user-Define functions
#4. Write your own user-defined functions

## USER-DEFINED FUNCTION
# It has two section
# function definition
# function call

# Example

def make_coffee():
 print("start machine")
 print("make coffee")
 print("Add Milk")
 print("Enjoy it")


print("Wake Up")
make_coffee()
print("Working for a while")
make_coffee()

import math
# Built-in function (just calling)
print(len("python"))

# Function from libraries (Import then call)
number = 4.2
print(math.ceil(number))

# User_Defined Function(Define then call)
def greet():
 print("hello")

greet()

# How data flows
# Shapes
# Parameters Names used in function definition that describe what data the function expects

# Arguments => This is the actual value passed in a function call
# that are assigned to parameters

# Difference between parameter
# 1. parameters are used in the function definition while argument are used in the function call
# 2. parameters are placeholders while argument are the actual value to fill in the placeholder
# 3. Defines what function expect while argument provides function with values