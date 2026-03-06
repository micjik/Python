# There are four types of data structure
# They are organized into four category according to their behaviour
# Ordered
# Duplicates
# Indexed
# Mutable

my_list = [10, 20, 30]
#LIST
print(my_list)
# In python list allows duplicates
# list are ordered
# list are indexed
# list are mutable, you can add, remove, update 
my_list[1] = 15
print(my_list)

#TUPLE
# It is an ordered collection that can not change after creating
# it used parenthesis
my_tuple = (10, 20, 30, 20)
print(my_tuple) # ordered, it allows duplicate, indexed, it is totally frozen
# it cannot be change once it is created.
# my_tuple[2] = 50 you cannot change any item in tuple once it is created
# it is immutable, if you want your data to be protected, you need tuple

#SET
# It is unorderd collection of unique values
# it is denoted with curly bracket

my_set = {10, 30, 20, 10}
print(my_set) #Unordered no duplicates
print(my_set[1]) # Not indexed 
my_set.remove(20) # set is mutable

#DIFFERENCES
#      ordered  Duplicates  Indexed  Mutable
#list   1         1           1        1
#Tuple  1         1           1        0
#Set    0         0           0        1
#dict   1         0 -keys
                # 1 - values  keys      1