# while condition:
# do something
#unknown times# While 
# Condition classical one
# True
i = 1 # initialization
while i < 5: # condition
    print(i) 
    i+=1     # increment i

count = 1
while count <= 5:
    print(count)
    count += 2

# Write a program that keeps asking
# Do you agree?
# Until the user type yes
inquiry = input("Do you agree")
while inquiry == "yes":
    print("thank you for your response")

answer = ""
while answer != "yes":
    answer = input("Do you agree? (yes/no): ")
print("thank you")

## True
while True:
    answer = input("Do you agree? (yes/no): ")
    if answer == "yes":
        break
print("Thank you")

# comparing while condition and while true
# while true ensure you use the if and break
# while condition => Exists normally, safer and more readable
# example counter, limited retries
# while True => must have extra if + break
# risk of infinite loop + more flexible
# open ended, waiting database streams

# difference between For and While
# for loop => used for loop over a fixed sequence, predefined condition, nr of iteration is known
# processing data, simple, clear, safe
# while loop => loop while a condition is True, number of iteration unknown
# waiting for external event, Advanced, flexible it could be * complex* *Risk"