"""Lab solution: Find Duplicate List Elements
Question number: 22
"""

items = input("Enter items separated by spaces: ").split()
seen, duplicates = set(), set()
for item in items:
    if item in seen: duplicates.add(item)
    seen.add(item)
print("Duplicates:", duplicates)
