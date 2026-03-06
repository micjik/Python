a = {10, 20, 30, 40}

a.add(50)
print(a)

a.update({1, 2})
a |= {1, 2}

a.remove(100) # this will give error if the value is not in set
#instead use this
a.discard(100)

a = {10, 20, 30,40}
b = {50, 60, 70, 80}
# mathematical operations
print(a.union(b))
print(a|b)

print(a.intersection(b))
print(a & b)

print(a.difference(b))
print(a - b)
print(b - a)

print(a.symmetric_difference(b))
print(a ^ b)

# Relationship Question
a = {30, 40}
b ={30, 40, 50, 60}
print(a.issubset(b))
print(b.issuperset(a))
# to do quality check use the issubset
print(a.isdisjoint(b))