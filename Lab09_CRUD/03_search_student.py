# Program 3: Search for a student by name
# Example I/O:
#   Input: riya
#   Output: Found: {'roll': 2, 'name': 'Riya', 'marks': 92}

# Student records: list of dictionaries
students = [
    {"roll": 1, "name": "Aman", "marks": 85},
    {"roll": 2, "name": "Riya", "marks": 92},
    {"roll": 3, "name": "Karan", "marks": 38},
]

name = input("Enter name to search: ").strip().lower()
for s in students:
    if s["name"].lower() == name:
        print("Found:", s)
        break
else:                                           # for-else: break na hua to chalega
    print("Student not found.")
