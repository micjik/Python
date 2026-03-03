for x in range(3): # outer loop
    for y in range(2): # inner loop
        print(f"{x}, {y}")


#Use cases
# Crossing Data
colors = ['red', 'blue', 'green']
sizes = ['L', 'M', 'S']
for color in colors:
    for size in sizes:
        print(f'{color} - {size}')

# Navigate Hierarchy
years = [2026, 2027]
months = ['jan', 'feb']
days = range(1, 29)

for y in years:
    for m in months:
        for d in days:
            print(f'report_{y}_{m}_{d}')

# iterating through tables
# SELECT count(*) FROM customers where is is NULL

tables = ['customers', 'orders', 'products', 'prices']
columns = ['id', 'create_date']
for t in tables:
    for c in columns:
        print(f"SELECT count(*) FROM {t} WHERE {c} IS NULL")