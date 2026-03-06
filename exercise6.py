user = {
    "id": 1,
    "name": "John",
    "age": 30,
    "city": "Berlin"
}
# create a new Dict
new_user = {
    #Expression
    k: v.upper()
    #Loop
    for k, v in user.items()
    # filter
    if isinstance(v, str)
}
# keep only pairs with string values

print(new_user)
