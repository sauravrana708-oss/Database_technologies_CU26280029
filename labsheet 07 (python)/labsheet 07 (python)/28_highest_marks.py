import csv, os
# Sample CSV banao agar nahi hai
if not os.path.exists("students.csv"):
    with open("students.csv", "w", newline="") as f:
        csv.writer(f).writerows([["Name", "Age", "Marks"], ["Aman", 20, 85], ["Riya", 21, 92], ["Karan", 20, 38], ["Neha", 22, 76]])

# Program 28: Find and display the highest marks from a CSV file
try:
    with open("students.csv", "r") as f:
        rows = list(csv.DictReader(f))
    top = max(rows, key=lambda r: int(r["Marks"]))      # Marks ke basis par max
    print(f"Highest marks: {top['Marks']} by {top['Name']}")
except FileNotFoundError:
    print("File not found.")
except ValueError:
    print("No valid data found.")
