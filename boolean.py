print(True)
print(False)
print(type(True))
print(bool(123))
print(bool("Hi"))
print(bool(0))
print(bool())
print(bool(""))
print(bool(None))
# Note that None is not the same as ""

#USING ANY OR ALL
email = ""
phone = "0176-123456"
username = ""
#Allow registration
#if any field is filled
print(any[email, phone, username])

#allow registration
#only if all fields are filled
print(all[email, phone, username])
isinstance(123, int)
print(isinstance(True, str))
print("Hello".endswith("o"))

#Comparison operator
#Compare value
# value operator value
print(3 > 2)
x = 12
print(x < 2)
#Expression 
len("Hi") == 3
print(10 == 10)
print(10 != 10)
print(7 > 3)
print("a" < "b")
print("A" == "a")
# = Assign
# == equal
print(1 < 4 < 6)

# is age between 18 and 30
age = 20
18 <= age <= age <= 30

#Logical Operator
#And|#or
#Used to Combine multipe boolean Operators
# and => both must be true
# or => one condition must be true
print(3 > 1 and 5 < 1)
print(3 > 1 and 5 > 1)

print(3 > 1 or 5 < 1)
print(3 > 1 or 5 > 1)
cpu_usage = 70
memory_usage = 95
print(cpu_usage > 90 or memory_usage > 90)

email = True
password = False
print(email and password)

#Not Operator
print(not 3 > 2)
print(not True)
print(not False)
print(not not False)
name = ""
print(not name)

# Allow access only if the user isLoggedIn
# or they are guest
# but they must not be banned
is_logged_in = True
is_guest = False
is_banned = False
print(is_logged_in or is_guest or is_banned)
print("a" not in "data")
#Membership identity(in & not in)
print("barra" not in ["Ayodele", "Bolaji", "Tunde"])
print(3 not in [1, 2, 3])

# Security check: ensure the domain is not banned
domain = "gmail.com"
banned_domains = ["spam.com", "fake.org", "bot.net"]
print(domain not in banned_domains)

#Identity (is) Operators
#to check if two variables refer to the same object in memory
#using a == b comparing values while a is b compare the id. they are pointing to the same id

x = ['a', 'b', 'c']
y = ['a', 'b', 'c']

print (x == y)
print (x is y)

# Make sure the email exists, and its not empty
email = None
print(email != None and email != "")
print(email is not None and email != "")
# Note Use is instead of == when checking for None