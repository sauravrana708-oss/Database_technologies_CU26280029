"""Lab solution: All Tuple Elements Same
Question number: 29
"""

items = tuple(input("Enter items separated by spaces: ").split())
print("All same" if not items or all(item == items[0] for item in items) else "Not all same")
