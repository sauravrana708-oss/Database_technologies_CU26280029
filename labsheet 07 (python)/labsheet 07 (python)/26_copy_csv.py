import csv, os
# Sample CSV banao agar nahi hai
if not os.path.exists("students.csv"):
    with open("students.csv", "w", newline="") as f:
        csv.writer(f).writerows([["Name", "Age", "Marks"], ["Aman", 20, 85], ["Riya", 21, 92], ["Karan", 20, 38], ["Neha", 22, 76]])

# Program 26: Copy data from one CSV file to another
try:
    with open("students.csv", "r") as src, open("students_copy.csv", "w", newline="") as dst:
        csv.writer(dst).writerows(csv.reader(src))
    print("Data copied to students_copy.csv")
except FileNotFoundError:
    print("Source file not found.")
