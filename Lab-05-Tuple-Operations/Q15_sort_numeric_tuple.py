"""Lab solution: Sort Numeric Tuple
Question number: 15
"""

numbers = tuple(float(x) for x in input("Enter numbers separated by spaces: ").split())
print(tuple(sorted(numbers)))
