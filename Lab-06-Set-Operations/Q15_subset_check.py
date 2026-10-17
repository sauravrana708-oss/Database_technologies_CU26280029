"""Lab solution: Subset Check
Question number: 15
"""

a = set(input("First set: ").split())
b = set(input("Second set: ").split())
print("First is subset of second" if a <= b else "First is not a subset of second")
