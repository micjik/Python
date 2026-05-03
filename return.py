# RETURN
# It is a tranformation function
def clean_name(name):
    if not name:
        return None
    else:
       cleaned = name.strip().lower()
       return cleaned # if no return, it will return None

cln_name = clean_name(" MariA ")
print(cln_name)

def clean_name(name):
    lo_cleaned = name.strip().lower()
    up_cleaned = name.strip().upper()
    return lo_cleaned, up_cleaned

l1, u2 = clean_name(" MariA ")

print(l1)
print(u2)

#Function Types by purpose
# Action Functions
# It is Designed to perform an operation in the system instead of returning values
# it is focused on the side Effect, do something outside of the function
# Example print, connect to Api, send something to the screen or call an API
# for example
# We want to store Application log messages in a file
# whenever an event happens
# Example of action function
def write_log(message):
    with open(r"c:\Users\micji\OneDrive\Desktop\Data_Engineering\Python\app.log", "a") as file:
        file.write(message + "\n")

write_log("App Started")
write_log("user logged in")
write_log("App Stopped")

# Transformation Functions
# Raw data goes in, gets transformed and returns processed data
# Raw data => processed data

# Task: clean email addresses and splits them into structured data
# return username abd domain
def clean_and_split_email(email):
    cl_email = email.strip().lower()
    #sara@gmail.com
    username, domain = cl_email.split("@")
    return {"username": username, "domain": domain}

print(clean_and_split_email("SARA@GMAiL.com "))

# Validation functions or checker function
# Validates a condition and returns a boolean result (True or False)
# check user input, check Business rules and check permissions

# Task: check if a password meets the minimum length of 8
def is_valid_password(password):
    return len(password) >= 8

print(is_valid_password("1234567"))
print(is_valid_password("123456789"))

# Task: check if eail has a basic valid format
def is_valid_email(email):
    return "@" in email and "." in email

print(is_valid_email("saragmail.com"))
print(is_valid_email("sara@gmail.com"))

#Orchestration functions
# It controls the flow of your program by calling other functions
# in the correct order. it is focused on the coordination, it represents the workflow

# Task:
#1 Receive an email from the user
#2 Validate the email
#3 if it is invalid, Log an error in a file
#4 if it is valid, clean and structure the email
#5 log each step of the program

#orchestrator function
def process_user_email(email):
    write_log("App Started")
    #is_valid_email(email)
    if not is_valid_email(email):
        write_log(f"Invalid Email received: {email}")
    else:
        clean_email = clean_and_split_email(email)
        write_log(f"Processed Email: {clean_email}")

    write_log("App Stopped")

email = input("Please enter your Email: ")
process_user_email(email)

# Function Styling coming from PEP8 - STYLE GUIDE
# PEP 8 RULES
# 1. Use Snake_case for function Names => write function names in lowercase
# and separate words with underscores
# example load data from file
# 2. use clear Descriptive function names
# - Describe exactly what the function does
# - start with a verb
# - use full words, avoid abbreviations
#3. Parameter Names Describe their values
# - use full, meaning words
# - Avoid abbreviations and single letters
#4. Always describe Functions using Docstring
# - Help teammates understand your code
# - help you in future to remember your logic
# Docstring is a short text on the first line inside a function
# that explains what the function does
#5. replace prints with return to send data back to the program
#6. Don't change parameter values directly, create local variables for any processing
#7. Use Data type Hints
# - Always add type hints to parameters and return to make
# the function easier to understand
#8. Explain Args and Return in Docstring
# - Always describe what goes in and what comes out of the function in the docstring
def calculate_discount(price: float, rate: float) -> float:
    """Calculate the final price after applying a discount.
    Args:
        price (float): original product price
        rate (float): Discount rate as numbers (e.g 20 for 20%)
    Returns:
        final_price (float): Final Price after applying discount
    """
    final_price = price - (price * rate/100)
    return final_price
