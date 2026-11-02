"""Lab solution: Repeated Items in Tuple
Question number: 28
"""

items = tuple(input("Enter items separated by spaces: ").split())
repeated = []
for item in items:
    if items.count(item) > 1 and item not in repeated: repeated.append(item)
print(tuple(repeated))
