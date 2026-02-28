#Numbers in python
# it belongs to primitive
#int 5 -12 10000
#float 3.15 -0.15 100.0
#complex 2 + 3j Advanced Math, Engineering, physics and science
import math
import random
x = 5
y = 5.7
z = 2 + 3j

print(type(x))
print(type(y))
print(type(z))

x = 2
y = 3

print(complex(x, y))

print(7 / 2)
print(7 // 2)
print(7 % 2)
print(2 ** 3)

x = 2
x += 3
print(x)
x -= 1
print(x)

# Measure Distance
print( abs(2 - 8))
#rounding numbers
price = 35.54879865
# round up goes to the one that is even
print(round(price))
print(round(price, 2))
print(math.floor(price))
print(math.ceil(price))
print(math.trunc(price))
print(int(price ))
print(random.random())

print(random.randint(1, 6))
# the random.randint() can be used to generate test data(dummy) for like gae, id, or prices

#Validation
x = 7.0
print(x.is_integer())
y = 7.1
print(y.is_integer())
x = 70
print(isinstance(x, int))
x = 70.4
print(isinstance(x, float))