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
#letters.clear() # remove everything
print(letters)
letters.remove('a') 
removed = letters.pop() # changing my list and return the removed value
#removed = letters.pop(1) # specify index number to remove
matrix. remove(['a', 'b', 'c'])
#matrix.pop()
#matrix[1].remove('e')
matrix[-1].pop(0)
matrix[0].pop()

# update
letters = ['a', 'b', 'c', 'd']
letters[0] = 'x'
letters[1] = 'y'
print(type(letters))

# how to sort 
# Rank by price
letters = ['c', 'a', 'b']
print(letters.sort())
letters.sort(reverse = True)

# With sort you are changing the original list
# while with sorted you are making a copy of the original list

letters = ['c', 'a', 'b']
new_list = sorted(letters)
print('original List:', letters)
print('Sorted List:', new_list)

## Reverse
letters = ['c', 'a', 'b']
letters.reverse()

# reversed # make a copy of the original 

## copying a data in python
#Reference
# shallow copy
# Deep copy
# copying list

letters = ['c', 'a', 'b']
letters_copy = letters
letters_copy.append('z')
print('original:', letters)
print('copying:', letters_copy) # it will affect the original list
#instead use copy
letters_copy = letters.copy()

matrix = [
    ['a', 'b'],
    ['c', 'd']
]
matrix_copy = matrix.copy()
matrix.pop()
matrix_copy[0].append('z')
print('original:', matrix)
print('copy: ', matrix_copy)

# the copy() method is a shallow copy you only get a copy for the top level which is the first level
# if you do anything to the deep level it will affect both original and copy one
# to be able to use the deep copy, you need to import copy
import copy
matrix = [
    ['a', 'b'],
    ['c', 'd']
]
matrix_copy = copy.deepcopy(matrix)
matrix.pop()
matrix_copy[0].append('z')
print('original:',  matrix)
print('copy: ', matrix_copy)
# another method from the import copy is just copy which is just like the shallow copy
matrix_copy = copy.copy(matrix) # shallow copy
## copy.copy() is more general that list.copy(), not limited to lists
original = [
    ['a', 'b'],
    ['c', 'd']
]
#Assignment
copy = original
print("Same object", original is copy, "\n")

#Shallow copy
copy2 = original.copy()
print("same object:", original is copy2)
print("Shared Lists", original[0] is copy[0], "\n")

# deep copy
copy3 = original
print("Same Object", original is copy3)
print("shared list", original[0] is copy3[0], "\n")

# How to Copy
# Avoid using Assignment Operator => Risky & Confusing
# Use .copy() for simple, flat lists
# use copy.deepcopy() for nested lists
# always make extra copy for Experiments/Tests