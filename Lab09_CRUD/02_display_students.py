# Program 2: Display all student records (Read)
# Example I/O:
#   Output: Roll: 1 | Name: Aman | Marks: 85

# Student records: list of dictionaries
students = [
    {"roll": 1, "name": "Aman", "marks": 85},
    {"roll": 2, "name": "Riya", "marks": 92},
    {"roll": 3, "name": "Karan", "marks": 38},
]

for s in students:
    print(f"Roll: {s['roll']} | Name: {s['name']} | Marks: {s['marks']}")
