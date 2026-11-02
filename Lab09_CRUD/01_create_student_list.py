# Program 1: Create a list of student records (Create)
# Example I/O:
#   Output: {'roll': 1, 'name': 'Aman', 'marks': 85} ...

students = []                                   # khali list
students.append({"roll": 1, "name": "Aman", "marks": 85})
students.append({"roll": 2, "name": "Riya", "marks": 92})
students.append({"roll": 3, "name": "Karan", "marks": 38})
print("Student records created:")
for s in students:
    print(s)
