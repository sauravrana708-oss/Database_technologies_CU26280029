import csv, os
# Sample CSV banao agar nahi hai
if not os.path.exists("students.csv"):
    with open("students.csv", "w", newline="") as f:
        csv.writer(f).writerows([["Name", "Age", "Marks"], ["Aman", 20, 85], ["Riya", 21, 92], ["Karan", 20, 38], ["Neha", 22, 76]])

# Program 24: Count the number of rows and columns in a CSV file
try:
    with open("students.csv", "r") as f:
        rows = list(csv.reader(f))
    print("Total rows (with header):", len(rows))
    print("Data rows               :", len(rows) - 1)
    print("Total columns           :", len(rows[0]) if rows else 0)
except FileNotFoundError:
    print("File not found.")
