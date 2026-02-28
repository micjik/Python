#check if a user's name is not empty and the age is greater than or equal to 18

user_name = "Ayodele"
age = 18
print(user_name is not None and age >= 18)

# check if the password is at least 8 characters long and does not contain spaces
password = "Darasimi8"
print(len(password) <= 8 and " " in password)
print(len(password) < 8 and password.isspace())

# check if a user's email is not empty, contains '@', and ends with '.com'
email = "micjik50@gmail.com"
print(email  != "" and '@' in email and email.endswith('.com'))

# check if a username is a string, is not None and is longer than 5 characters
user_name = "Ayodele"
print(isinstance(user_name, str) and user_name is not None and len(user_name) > 5)

#check if the user is either an admin or moderator and check if they are not banned or they have verified their email
user = "admin"
is_banned = False
is_email_verified = True
print(user == "admin" or is_banned or is_email_verified )