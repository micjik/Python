# Positional Arguments
# Values pass to the function based on their order

# Keyword Arguments
# values pass to the function based on their names

def cleaned_full_name(first_name, last_name, country):
    first = first_name
    last = last_name
    full_name = first + " " + last

    print(f"My fullname is: {full_name} From {country}")
# positional Arguments 2 -3 Arguments
cleaned_full_name(" MAriA ", "  SMITH ", "DE")

#Keyword Arguments greater than 3 arguments
cleaned_full_name(country = "DE", first_name = " MAriA ", last_name = " SMITH ")

#Mix Arguments you must start with positional - rule
cleaned_full_name(" MariA ", last_name = " SMITH ", country = "DE")

# Default Parameter
# Parameters that has already a value so if you don't pass anything
# in python uses that value automatically

# Sometimes in python you don't know how many arguments will be passed to your function
# we have the *args and **kwargs
# they allow functions to accept an unknown number of arguments

# cal the total of values
def total(*args):
    print(sum(args)) # tuple
    print(type(args))

total(1, 2)
total(1, 2, 3)
total(1, 2, 3, 4)
# When to use *args
# when you pass similar values like (1, 2, 3, 4, 5) or
# (Alex, Kumar, Nora, Omar, Leo)
# but when you pass different types of values you use **kwargs

# Create the user profile
def create_user(**kwargs):
    print(type(kwargs)) # dictionary

create_user(first_name = "MO",
            last_name = "Salah",
            age = 33,
            country = "Egypt")

# difference between *args and **kwargs
#    *args                               **kwargs
# 1  positional argument              keyword arguments
# 2  only values                      Names of values
# 3  same type of information         Different type of information
# 4  Tuple                            Dictionary