"""Lab solution: Membership Check
Question number: 08
"""

items = set(input("Enter set items separated by spaces: ").split())
item = input("Element to check: ")
print("Exists" if item in items else "Does not exist")
