# Program 5: Delete a student record by roll number (Delete)
# Example I/O:
#   Input: 3
#   Output: Record deleted.

# Student records: list of dictionaries
students = [
    {"roll": 1, "name": "Aman", "marks": 85},
    {"roll": 2, "name": "Riya", "marks": 92},
    {"roll": 3, "name": "Karan", "marks": 38},
]

try:
    roll = int(input("Enter roll number to delete: "))
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Record deleted.")
            break
    else:
        print("Roll number not found.")
    print(students)
except ValueError:
    print("Please enter a number.")
