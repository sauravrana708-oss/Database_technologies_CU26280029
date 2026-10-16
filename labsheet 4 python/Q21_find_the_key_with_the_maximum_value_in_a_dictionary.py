# Q21: Find the key with the maximum value in a dictionary
data = {"Aman": 78, "Riya": 92, "Karan": 65}
if data:
    iterator = iter(data)
    best_key = next(iterator)
    for key in iterator:
        if data[key] > data[best_key]:
            best_key = key
    print("Key with maximum value:", best_key)
    print("Maximum value:", data[best_key])
else:
    print("Dictionary is empty.")
