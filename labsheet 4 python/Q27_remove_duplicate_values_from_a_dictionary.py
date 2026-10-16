# Q27: Remove duplicate values from a dictionary (keep first occurrence)
data = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
result = {}
seen_values = []
for key, value in data.items():
    if value not in seen_values:
        result[key] = value
        seen_values.append(value)
print("Original dictionary:", data)
print("Without duplicate values:", result)
