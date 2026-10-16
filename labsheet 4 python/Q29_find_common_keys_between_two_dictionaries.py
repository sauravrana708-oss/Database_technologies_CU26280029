# Q29: Find common keys between two dictionaries
first = {"name": "Aman", "age": 21, "course": "MCA"}
second = {"name": "Riya", "course": "BCA", "city": "Roorkee"}
common_keys = []
for key in first:
    if key in second:
        common_keys.append(key)
print("Common keys:", common_keys)
