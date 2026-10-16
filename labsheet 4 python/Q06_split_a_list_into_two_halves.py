# Q06: Split a list into two halves
items = input("Enter list items separated by spaces: ").split()
middle = (len(items) + 1) // 2
print("First half:", items[:middle])
print("Second half:", items[middle:])
