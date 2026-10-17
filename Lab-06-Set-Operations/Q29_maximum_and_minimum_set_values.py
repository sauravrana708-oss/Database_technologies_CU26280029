"""Lab solution: Maximum and Minimum Set Values
Question number: 29
"""

numbers = {float(x) for x in input("Enter numbers separated by spaces: ").split()}
if numbers: print("Maximum:", max(numbers), "Minimum:", min(numbers))
else: print("Set is empty")
