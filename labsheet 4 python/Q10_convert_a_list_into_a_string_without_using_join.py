# Q10: Convert a list into a string without using join()
items = input("Enter list items separated by spaces: ").split()
result = ""
for index, item in enumerate(items):
    if index > 0:
        result += " "
    result += item
print("String:", result)
