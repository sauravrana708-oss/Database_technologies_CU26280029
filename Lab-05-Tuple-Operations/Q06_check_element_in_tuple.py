"""Lab solution: Check Element in Tuple
Question number: 06
"""

items = tuple(input("Enter items separated by spaces: ").split())
item = input("Element to find: ")
print("Found" if item in items else "Not found")
