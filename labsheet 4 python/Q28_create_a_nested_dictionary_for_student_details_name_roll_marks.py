# Q28: Create a nested dictionary for student details
students = {
    1: {"Name": "Aman", "Roll": 101, "Marks": 82},
    2: {"Name": "Riya", "Roll": 102, "Marks": 91}
}
for student_id, details in students.items():
    print("Student", student_id, ":", details)
