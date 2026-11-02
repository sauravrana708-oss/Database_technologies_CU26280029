"""Lab solution: Tuple to String
Question number: 12
"""

items = tuple(input("Enter tuple items: ").split())
result = ""
for item in items: result += item
print(result)
