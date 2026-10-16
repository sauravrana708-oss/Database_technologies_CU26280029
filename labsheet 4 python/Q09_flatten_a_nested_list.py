# Q09: Flatten a nested list (one level deep)
nested = [[1, 2], [3, 4], [5, 6]]
flattened = []
for sublist in nested:
    for item in sublist:
        flattened.append(item)
print("Nested list:", nested)
print("Flattened list:", flattened)
