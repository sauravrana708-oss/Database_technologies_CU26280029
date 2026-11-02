# Program 4: Update a student's marks (Update)
# Example I/O:
#   Input: roll=3, marks=55
#   Output: Marks updated.

# Student records: list of dictionaries
students = [
    {"roll": 1, "name": "Aman", "marks": 85},
    {"roll": 2, "name": "Riya", "marks": 92},
    {"roll": 3, "name": "Karan", "marks": 38},
]

try:
    roll = int(input("Enter roll number: "))
    marks = int(input("Enter new marks: "))
    for s in students:
        if s["roll"] == roll:
            s["marks"] = marks
            print("Marks updated.")
            break
    else:
        print("Roll number not found.")
    print(students)
except ValueError:
    print("Please enter numbers only.")
