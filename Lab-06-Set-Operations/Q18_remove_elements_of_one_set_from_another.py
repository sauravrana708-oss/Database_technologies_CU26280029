"""Lab solution: Remove Elements of One Set from Another
Question number: 18
"""

a = set(input("Main set: ").split())
b = set(input("Elements to remove: ").split())
print(a - b)
