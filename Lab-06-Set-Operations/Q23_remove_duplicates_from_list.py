"""Lab solution: Remove Duplicates from List
Question number: 23
"""

items = input("Enter items separated by spaces: ").split()
print(list(dict.fromkeys(items)))
