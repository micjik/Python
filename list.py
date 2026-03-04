# A list is an ordered collection of items
# changeable
# Allows duplicates
# how to create 
# how to access and read
# how to unpack
# how to explore and analyze
# how to change
# how to order
# how to copy
# how to combine
# how to iterate
# how to tranform
# how to gilter
# list of comprehension

## How to craete an empty list
empty = []
print(empty)
print(type(empty))
# invariable python will create an object in memory which has an empty value
# create a list be adding items manually
letters = [ 'a', 'b', 'c']
print(letters)
numbers = [1, 2, 3, 4]
# inside list you can have mixed data types
mixed = [1, 'a', True, None]
# another way to create list is list()
# create Lists
empty = list()
print(empty)
letters = list('python')
print(letters)
numbers = list(range(5))
print(numbers)
# procreate
matrix = [['a', 'b', 'c'], ['d', 'e', 'f']]
mixed_matrix = [['a', 'b'],
                [1, 2, 3],
                ['ab', 'cd']
                ]

## How to Access and Read
list = ['a', 'b', 'c', 'd']
print(list)
print(list[0]) # to access first item
print(list[-1]) # to access last item

## how to access matrix
matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]
print(matrix)
print(matrix[-1])
print(matrix[-1][2])
print(matrix[0][0])
print(matrix[:2])
print(matrix[1:])
print(matrix[2][:2])

# Slicing
letters = ['a', 'b', 'c', 'd']
print(list[0:3])
print(list[:]) # give you everything

## Unpack List
# use case of unpacking
person = ['maria', 29, 'Data Engineer', 'spain']
name, age, role, country = person
print(name)
name, *details, country = person # allow to use one asterick 
print(details)
print(country)
# Rule for Unapcking
# 1. Nr of variables must match the values exactly
# 2 Asterick collects leftover and its fine if there are none
person = ['maria', 29, 'Data Engineer', 'spain']
name, _, role, _ = person # the underscore does not store any value, you dont want the other values
name, *_, country = person

## how to analyze and explore
## Functions
numbers = [1, 5, 2, 4, 3]
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sum:", sum(numbers))
print("Length:", len(numbers))

print("All:", all(numbers))
print("All:", all([1, 0, 2]))
print("All:", all(['a', '', 'b']))
print("All:", all(['a', 'c', 'b']))

print("Any:", any(numbers))
print("All:", any([1, 0, 2]))

## Methods
numbers = [1, 5, 5, 4, 3]
print("count:", numbers.count(5))
print("Index:", numbers.index(5))
print(4 in numbers)
print(8 not in numbers)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)
print(list1 is list2) # if they are pointing to the same address in the memory

## changing list
## adding item to your 
## Using append
letters = ['a', 'b', 'c']
letters.append('d')
letters.append('x')
#.append(value) add item at the end
## using insert method
# .insert(index, value) Add item at specific position
letters.insert(0, 'x')
letters.insert(3, 'y')

matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]
matrix.append( ['x', 'y', 'z'])
matrix.insert(3, (['j', 'h', 'k']))

## how to remove item from the list
# duplicate, bad data and old data
letters = ['a', 'b', 'c']
letters.clear() # remove everything
print(letters)
letters.remove('a') 
removed = letters.pop() # changing my list and return the removed value
removed = letters.pop(1) # specify index number to remove
matrix. remove(['a', 'b', 'c'])
#matrix.pop()
matrix[1].remove('e')
matrix[-1].pop(0)
matrix[0].pop()



