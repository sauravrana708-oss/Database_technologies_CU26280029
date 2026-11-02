"""Lab solution: Swap Two Tuples
Question number: 23
"""

a = tuple(input("First tuple items: ").split())
b = tuple(input("Second tuple items: ").split())
a, b = b, a
print("First:", a)
print("Second:", b)
