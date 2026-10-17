"""Lab solution: Add Multiple Elements
Question number: 04
"""

items = set(input("Enter set items separated by spaces: ").split())
more = set(input("Enter more items separated by spaces: ").split())
items.update(more)
print(items)
