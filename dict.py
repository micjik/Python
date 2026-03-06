# list, tuple, set are stored in a single form
# In reality we use dictionary in the real world
my_dict = {
    'a': 10,
    'b': 20,
    'c': 30,
    'd': 20
}
print(my_dict) # It is ordered # keys are unique, values allow duplicates
print(my_dict['b']) # not indexed(keyed)
my_dict['c'] = 80
print(my_dict)

#Special Method for Dictionary
user = {'id': 1, 'age': 30, 'city': 'berlin'}
#Access#
print(user['age'])
print(user.get("name", "unknown"))

#checks
print("age" in user)
print("name" not in user)

#View objects
print(user.keys())
print(user.values())
print(user.items()) # it gives you a list of tuples

#Looping
for u in user:
    print(u)

for key, value in user.items():
    print(key, value)

# Add, Remove, Update
user['name'] = 'John' # Add
print(user) 
user['age'] = 35 # update
user.update({"age": 40, "city": "paris"})
print(user)

age = user.pop("age")
print(user)
age = user.pop("salary", "Not Found") # if your key is not present and in order to be save

user.popitem()
#Creation
user = {
    "id": None,
    "name": None,
    "age": None,
    "city": None
}
user = dict.fromkeys(["id", "name", "age", "city"], None)

# Real Time Application
#1 Database or API Records
#Returned records are stored as dictionary where column names are keys
# and the row values are the dictionary rows
# Representing a single row from a database or API
row = {
    "id": 101,
    "name": "John",
    "country": "DE",
    "age": 29,
    "status": "active"
}
#2 Mapping to Friendly values
# Great for converting techncical codes into friendly labels
status_map = {
    "01": "open",
    "02": "In progress",
    "03": "Done"
}
#3 Mapping Abbreviation
# Turning short abbreviation into full readable names
country = {
    "uk": "United Kingdom",
    "usa": "United State of America",
    "de": "Denmark",
    "ng": "Nigeria"
}
#4 Config and Environment Data
# Store system setting LIKE HOST, PORT USERNAME IN ONE CLEAN PLACE
# Storing environment variables & configuration
env_config = {
    "DB_HOST": "prod-db.company.com",
    "DB_PORT": 5432,
    "DB_USER": "admin_user",
    "DB_NAME": "analytic_warehouse"
}
#5 ETL AND PIPELINE SETTING
# Great fr storing run parameters and controlling how your ETL pipeline loads data