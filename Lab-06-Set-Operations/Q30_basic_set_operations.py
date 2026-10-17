"""Lab solution: Basic Set Operations
Question number: 30
"""

a = set(input("First set: ").split())
b = set(input("Second set: ").split())
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference (A-B):", a - b)
print("Symmetric difference:", a ^ b)
