"""Lab solution: Common Tuple Elements
Question number: 24
"""

a = tuple(input("First tuple items: ").split())
b = tuple(input("Second tuple items: ").split())
print(tuple(item for item in a if item in b))
