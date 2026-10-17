"""Lab solution: Disjoint Sets
Question number: 17
"""

a = set(input("First set: ").split())
b = set(input("Second set: ").split())
print("Disjoint" if a.isdisjoint(b) else "Not disjoint")
