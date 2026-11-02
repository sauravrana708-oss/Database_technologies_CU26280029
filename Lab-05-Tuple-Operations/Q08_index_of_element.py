"""Lab solution: Index of Element
Question number: 08
"""

items = tuple(input("Enter items separated by spaces: ").split())
item = input("Element to find: ")
try: print("Index:", items.index(item))
except ValueError: print("Element not found")
