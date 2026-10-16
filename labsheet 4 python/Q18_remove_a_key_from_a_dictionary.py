# Q18: Remove a key from a dictionary
data = {"name": "Aman", "age": 21, "course": "MCA"}
key = input("Enter key to remove: ")
if key in data:
    del data[key]
    print("Updated dictionary:", data)
else:
    print("Key not found.")
