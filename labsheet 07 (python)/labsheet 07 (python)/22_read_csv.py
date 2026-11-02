import csv, os
# Sample CSV banao agar nahi hai
if not os.path.exists("students.csv"):
    with open("students.csv", "w", newline="") as f:
        csv.writer(f).writerows([["Name", "Age", "Marks"], ["Aman", 20, 85], ["Riya", 21, 92], ["Karan", 20, 38], ["Neha", 22, 76]])

# Program 22: Read data from a CSV file and display it
try:
    with open("students.csv", "r") as f:
        for row in csv.reader(f):
            print(row)
except FileNotFoundError:
    print("File not found.")
