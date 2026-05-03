
def clean_name():
    name = " Maria "
    print(name.strip().lower())

# Instead use this because you could use another name

def clean_name(name):
    print(name.strip().lower())

clean_name("Maria")
clean_name("Kumar")
clean_name("Ayodele")

# Differences between local variables, global variables and parameters

# Global variable is created outside the function and can be accessed anywhere
# Local variable is created inside the function and can be accessed only inside the function

#    Global           Local                    Parameters
#    lives in the     lives during              lives during the function
#   whole program     function Execution
#   Accessed Anywhere  Accessed only inside fn  Accessed only inside fn

# Example 2:
def cleaned_name(name): # name == parameter
    cleaned = name.strip().lower() # == local variable
    print("raw: ", name)
    print("Cleaned: ", cleaned)

cleaned_name("MariA")


# Including global variable
case_rule = "lower" # global variable
def clean_name(name):
    cleaned = name.strip()
    if case_rule == "lower":
        cleaned = cleaned.lower()
    print("Cleaned: ", cleaned)

clean_name(" MariA ")
print("The Rule is: ", case_rule)


# Example 3

