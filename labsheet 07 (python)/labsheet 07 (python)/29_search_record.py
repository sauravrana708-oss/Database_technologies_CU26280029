import csv, os
# Sample CSV banao agar nahi hai
if not os.path.exists("students.csv"):
    with open("students.csv", "w", newline="") as f:
        csv.writer(f).writerows([["Name", "Age", "Marks"], ["Aman", 20, 85], ["Riya", 21, 92], ["Karan", 20, 38], ["Neha", 22, 76]])

# Program 29: Search a record in a CSV file based on student name
try:
    name = input("Enter student name: ").strip().lower()
    found = False
    with open("students.csv", "r") as f:
        for row in csv.DictReader(f):
            if row["Name"].lower() == name:
                print("Record found:", dict(row))
                found = True
    if not found:
        print("Record not found.")
except FileNotFoundError:
    print("File not found.")
