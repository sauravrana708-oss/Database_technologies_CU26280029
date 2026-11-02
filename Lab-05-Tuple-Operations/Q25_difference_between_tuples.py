"""Lab solution: Difference Between Tuples
Question number: 25
"""

a = tuple(input("First tuple items: ").split())
b = tuple(input("Second tuple items: ").split())
print(tuple(item for item in a if item not in b))
