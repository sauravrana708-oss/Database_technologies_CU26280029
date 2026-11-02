import csv, os
# Sample CSV banao agar nahi hai
if not os.path.exists("students.csv"):
    with open("students.csv", "w", newline="") as f:
        csv.writer(f).writerows([["Name", "Age", "Marks"], ["Aman", 20, 85], ["Riya", 21, 92], ["Karan", 20, 38], ["Neha", 22, 76]])

# Program 25: Append a new record to an existing CSV file
try:
    name = input("Name: ")
    age = int(input("Age: "))
    marks = int(input("Marks: "))
    with open("students.csv", "a", newline="") as f:    # "a" = append
        csv.writer(f).writerow([name, age, marks])
    print("Record added.")
except ValueError:
    print("Age and Marks must be numbers.")
