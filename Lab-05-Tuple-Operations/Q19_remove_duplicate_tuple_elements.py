"""Lab solution: Remove Duplicate Tuple Elements
Question number: 19
"""

items = tuple(input("Enter items separated by spaces: ").split())
unique = []
for item in items:
    if item not in unique: unique.append(item)
print(tuple(unique))
