# Q02: Rotate a list by n positions (left rotation)
items = input("Enter list items separated by spaces: ").split()
n = int(input("Enter number of positions to rotate left: "))
if items:
    n %= len(items)
    rotated = items[n:] + items[:n]
    print("Rotated list:", rotated)
else:
    print("The list is empty.")
