import csv, os
# Sample CSV banao agar nahi hai
if not os.path.exists("students.csv"):
    with open("students.csv", "w", newline="") as f:
        csv.writer(f).writerows([["Name", "Age", "Marks"], ["Aman", 20, 85], ["Riya", 21, 92], ["Karan", 20, 38], ["Neha", 22, 76]])

# Program 23: Calculate the average of numeric columns in a CSV file
try:
    totals, counts = {}, {}
    with open("students.csv", "r") as f:
        for row in csv.DictReader(f):       # har row dictionary
            for col, val in row.items():
                try:
                    num = float(val)        # numeric ho to hi count karo
                except ValueError:
                    continue                # text column (Name) skip
                totals[col] = totals.get(col, 0) + num
                counts[col] = counts.get(col, 0) + 1
    for col in totals:
        print(f"Average of {col}: {totals[col] / counts[col]:.2f}")
except FileNotFoundError:
    print("File not found.")
