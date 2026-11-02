"""Lab solution: Flatten Nested Tuple
Question number: 22
"""

nested = ((1, 2), (3, 4), (5, 6))
flat = tuple(item for inner in nested for item in inner)
print(flat)
