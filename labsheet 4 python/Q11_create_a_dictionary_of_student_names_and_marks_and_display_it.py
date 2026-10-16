# Q11: Create a dictionary of student names and marks and display it
count = int(input("How many students? "))
students = {}
for _ in range(count):
    name = input("Student name: ")
    marks = float(input("Marks: "))
    students[name] = marks
print("Student marks:", students)
