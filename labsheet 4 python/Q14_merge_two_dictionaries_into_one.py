# Q14: Merge two dictionaries into one
first = {"a": 1, "b": 2}
second = {"b": 3, "c": 4}
merged = first.copy()
for key, value in second.items():
    merged[key] = value
print("Merged dictionary:", merged)
