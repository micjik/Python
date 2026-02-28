# validate the quality and correctness of Email Values
# Must not be empty
# must contain "." and "@"
# must contain exactly one "@" symbol
# must end with ".com", ".org", or ".net"
# must not be longer than 254 characters
# must end or start with letter or digits

email = "Ayomide5@gmail.com"
# Clean the string
email = email.strip()
if email == "":
    print("it must not be empty")
if "." not in email and "@" not in email:
    print("It must contain @ and .")
if email.count("@") != 1:
    print("the email must contain only one @")
if not email.endswith(".com" ".org" ".net"):
    print("It must end with .com, .net, .com")
if len(email) > 254:
    print("It must not be longer than 254")
if not (email[0].isalnum() and email[-1].isalnum()):
    print("must start or end with digit or string")
else:
    print("Print the email is valid and correct", email)


#Exercise:
# Validate the quality and correctness of passwords
# must not be empty
# must be atleast 8 characters
# must include at least 1 uppercase
# must include at least 1 lowercase
# must not be same as the email
# must not contain ant spaces
# must start and end with letter or digit

password = ""
email = ""
#cleaning the string
password = password.strip()

if password == "":
    print("password should not be empty")
if len(password) < 8:
    print("password must contain at least 8 characters")
if not(any(char.issuper() for char in password)):
    print("password must contain an uppercase character")
if not(any(char.islower() for char in password)):
    print("Password must contain atleast one lower case")
if password == email:
    print("password cannot have the same value as email")
if " " in password:
    print("password should not contain spaces")
if password[0].isalnum() and password[-1].isalnum():
    print("password must start or end with string or number")
else:
    print("password is valid")