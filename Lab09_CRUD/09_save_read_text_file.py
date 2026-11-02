# Program 9: Save student data into a text file and read it back
# Example I/O:
#   File line format: roll,name,marks

# Student records: list of dictionaries
students = [
    {"roll": 1, "name": "Aman", "marks": 85},
    {"roll": 2, "name": "Riya", "marks": 92},
    {"roll": 3, "name": "Karan", "marks": 38},
]

try:
    with open("students.txt", "w") as f:            # save
        for s in students:
            f.write(f"{s['roll']},{s['name']},{s['marks']}\n")
    print("Data saved to students.txt\n")
    with open("students.txt", "r") as f:            # read back
        for line in f:
            roll, name, marks = line.strip().split(",")
            print(f"Roll: {roll} | Name: {name} | Marks: {marks}")
except IOError as e:
    print("File error:", e)
