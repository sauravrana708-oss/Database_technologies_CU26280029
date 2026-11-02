"""Lab solution: Maximum and Minimum Tuple Values
Question number: 13
"""

numbers = tuple(float(x) for x in input("Enter numbers separated by spaces: ").split())
if numbers: print("Maximum:", max(numbers), "Minimum:", min(numbers))
else: print("Tuple is empty")
