"""Lab solution: Cartesian Product
Question number: 20
"""

a = set(input("First set: ").split())
b = set(input("Second set: ").split())
print({(x, y) for x in a for y in b})
