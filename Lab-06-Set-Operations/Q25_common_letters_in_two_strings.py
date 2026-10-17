"""Lab solution: Common Letters in Two Strings
Question number: 25
"""

a = set(input("First string: ").lower())
b = set(input("Second string: ").lower())
print(a & b)
