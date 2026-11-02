"""Lab solution: Sort Strings Alphabetically
Question number: 16
"""

items = tuple(input("Enter words separated by spaces: ").split())
print(tuple(sorted(items, key=str.lower)))
