# how to combine data
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
comb = letters + numbers
print(comb)
print(comb * 2)
#Nested list
comb2 = [letters, numbers]
print(comb2)
numbers.extend(letters) # we just change and extended one of the list
print(numbers)

comb_3 = list(zip(letters, numbers, "Hi"))
print(comb_3)

ids = [101, 102, 103]
names = ['Ali', 'Sara', 'John']
print(list(zip(ids, names)))

## ITERATORS & ITERABLE
# HOW TO ITERATE
# WHY DO WE NEED ITERATOR
# 1. To build a loop
# 2. to save memory
# 3. speed and flexibility
# what is iterable => it is the object like a list we can loop over
# Iterator is the process or machine that helps us do iterate
letters = ['a', 'b', 'c', 'd']
for l in letters:
    print(l)

new_list = []
for l in letters:
    new_list.append(l.upper())
    print(new_list)

# enumerate ( Iterable) # to find bad data in your list

print(list(enumerate(letters, start = 1)))
for index, value in enumerate(letters):
    print(index, value)

print(reversed(letters))
for l in letters:
    print(l)

    letters = ['a', 'b', 'c', 'd']
    numbers = [1, 2, 3]
    for l, n in list((zip(letters, numbers))):
        print(l, n)

## MAP ITERATOR
# MAP(FUNCTION, ITERABLE)
letters = ['a', 'b', 'c', 'd']
print(list(map(str.upper, letters)))

numbers = ['1', '2', '3']
print(list(map(int, numbers)))

names = [' Maria', 'John ', ' Kumar']
print(list(map(str.strip, names)))
# OR
for name in map(str.strip, names):
    print(name)

# FILTERS
#filter(function, iterable)
letters = ['a', '',  'b', None, 'c', 'd', False]
print(list(filter(None, letters)))
print(list(filter(bool, letters)))

items = ['sql', '123', 'python', '42']
print(list(filter(str.isalpha, items)))

#lambda function
multiply = lambda x: x * 2
print(multiply(2))

add = lambda x, y: x + y
print(add(1, 2))

check = lambda i: i in "python"
print(check('n'))

#Lambda + Map
prices = ['$12.50', '$9.99', '$100.00']
print(list(map(lambda p: float(p.replace('$', '')), prices)))

p = '$12.50' #start building the logic by starting one single item
print((type(float(p.replace('$', '')))))

# Lambda + Filter
prices = [120, 30, 300, 80]
list(filter(lambda p: p >= 100, prices))

#p >= 100 # start building the logic by starting one single item

students = [['Maria', 85],
            ['Kumar', 90],
            ['Max', 60]
            ]
print(students[0][1] > 70) # start building the logic by starting one single item
list(filter(lambda row: row[1] > 70, students))

#print(students[0][0]).startswith('M')
print(list(filter(lambda row: row[0].startswith('M'), students)))

## List Comprehension => Advanced Concept
# We can loop, filter, transform data
# data transformation p * 2 step 3
# loop P for prices step 1
# filter if p > 50 step 2

domains = ['www.google.com',
          'openai.com',
          'localhost',
          'WWW.DATAWITHBARAA.COM']
cleaned = [
    d.lower().replace('www.', '')
    for d in domains
    if '.' in d
]
print(cleaned)