"""Lab solution: Element-wise Sum of Tuples
Question number: 30
"""

a = tuple(int(x) for x in input("First tuple integers: ").split())
b = tuple(int(x) for x in input("Second tuple integers: ").split())
if len(a) != len(b): print("Tuples must have equal length")
else: print(tuple(x + y for x, y in zip(a, b)))
