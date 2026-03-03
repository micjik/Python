# There are two types of loop in python
items = (1, 2, 3, 4, 5)
for item in items :
    print("Round ", item)

# i is loop variable
# (1, 2, 3) is a sequence
# python iterator is an object that lets you go through items one by one in a sequence
# you can use tuple = ((1, 2, 3, 4, 5), list = [1, 2, 3, 4, 5], string = "hello" range
# range(start, stop, step)
for item in range(5):
    print(item)

for item in range(1, 5):
    print(item)

for item in range(1, 10, 2):
    print(item)

# use case scenario
# We use loops to go through values and aggregate data like summing, counting, or averaging
scores = [80, 50, 60, 75]
total = 0
for score in scores:
    print(total = total + score)

# We use for loops to tranform data like cleaning data before processing
files = [' Report.csv ', ' DATA.csv ', ' final.TXT ']
for file in files:
    file = file.strip().lower().replace('.txt', '.csv')