"""Lab solution: Tuple Indexing
Question number: 04
"""

items = tuple(input("Enter items separated by spaces: ").split())
index = int(input("Index (0-based): "))
try: print(items[index])
except IndexError: print("Index out of range")
