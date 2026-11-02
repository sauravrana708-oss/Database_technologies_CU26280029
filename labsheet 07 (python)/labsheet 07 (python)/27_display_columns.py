import csv, os
# Sample CSV banao agar nahi hai
if not os.path.exists("students.csv"):
    with open("students.csv", "w", newline="") as f:
        csv.writer(f).writerows([["Name", "Age", "Marks"], ["Aman", 20, 85], ["Riya", 21, 92], ["Karan", 20, 38], ["Neha", 22, 76]])

# Program 27: Display specific columns (Name and Marks) from a CSV file
try:
    with open("students.csv", "r") as f:
        print(f"{'Name':<10}{'Marks':>5}")
        for row in csv.DictReader(f):
            print(f"{row['Name']:<10}{row['Marks']:>5}")
except FileNotFoundError:
    print("File not found.")
