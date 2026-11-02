"""Lab solution: Tuple Slicing
Question number: 05
"""

items = tuple(input("Enter items separated by spaces: ").split())
start = int(input("Start index: "))
stop = int(input("Stop index: "))
print(items[start:stop])
