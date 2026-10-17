"""Lab solution: Superset Check
Question number: 16
"""

a = set(input("First set: ").split())
b = set(input("Second set: ").split())
print("First is superset of second" if a >= b else "First is not a superset of second")
