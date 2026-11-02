"""Lab solution: Nested Tuple Access
Question number: 21
"""

nested = ((1, 2), (3, 4), (5, 6))
print("Nested tuple:", nested)
row = int(input("Tuple index (0-2): "))
col = int(input("Element index (0-1): "))
try: print(nested[row][col])
except IndexError: print("Index out of range")
