"""Lab solution: Remove with discard()
Question number: 06
"""

items = set(input("Enter set items separated by spaces: ").split())
items.discard(input("Element to discard: "))
print(items)
