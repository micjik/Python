attempts = 0
while attempts < 3:
    answer = input("Do you agree? (yes/no): ")
    if answer == "yes":
        print("print Glad we are on the same page")
        break
    attempts += 1
else:
    print("3 strikes. You're out")

# Allow up to 3 attempts
# if the user types "yes" print Glad we are on the same page
# Otherwise "3 strikes. You're out"