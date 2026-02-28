# if defines the first condition
# onely one if
# starts with if
# required
#can standalone
score = 100
if score > 90:
    print("A")
    print("Great job!")
else:
    print("F")

#else runs only if all previous conditions are false "if nothing was true do this instead"
# comes at the end
# No conditions
#optional
#cannot standalone

#Multi condition elif follow up questions
# comes after if statement
# multiple elif
# Needs condition
# optional
score = 95
submitted_project = True
if score >= 90 and submitted_project:
    print("A+")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60 or not submitted_project:
    print("D")
else:
    print("F")

# Nested if Statement
  
# Independent ifs Statement
score = 50
submitted_project = False

if score <= 90:
    print("High Score")
else:
    print("Low Score")

if submitted_project:
    print("project is Submitted")
else:
    print("project not submitted")

# one inline
grade = "A" if score >= 90  else "B" if score >= 80 else "F"
print(grade)

# match case
country = "United States"
if country == "United States":
    print("US")
elif country == "India":
    print("IN")
elif country == "Germany":
    print("DE")
elif country == "Egypt":
    print("EG")
else:
    print("Unknown country")

# how the match case works it is working one on one
match country:
    case "United States":
        print("US")
    case "Germany":
        print("DE")
    case "Egypt":
        print("DE")
    case "India":
        print("IN")
    case _:
        print("Unknown Country")
