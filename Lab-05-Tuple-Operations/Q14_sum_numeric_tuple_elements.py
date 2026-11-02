"""Lab solution: Sum Numeric Tuple Elements
Question number: 14
"""

numbers = tuple(float(x) for x in input("Enter numbers separated by spaces: ").split())
print("Sum:", sum(numbers))
