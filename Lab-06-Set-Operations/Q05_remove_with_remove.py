"""Lab solution: Remove with remove()
Question number: 05
"""

items = set(input("Enter set items separated by spaces: ").split())
item = input("Element to remove: ")
try: items.remove(item)
except KeyError: print("Element not found")
print(items)
