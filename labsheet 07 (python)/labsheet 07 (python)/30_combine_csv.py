import csv, os
# Sample CSV banao agar nahi hai
if not os.path.exists("students.csv"):
    with open("students.csv", "w", newline="") as f:
        csv.writer(f).writerows([["Name", "Age", "Marks"], ["Aman", 20, 85], ["Riya", 21, 92], ["Karan", 20, 38], ["Neha", 22, 76]])

# Program 30: Combine multiple CSV files into one single file
# Demo ke liye doosri CSV banao
if not os.path.exists("students2.csv"):
    with open("students2.csv", "w", newline="") as f:
        csv.writer(f).writerows([["Name", "Age", "Marks"], ["Rohit", 21, 67], ["Sneha", 20, 91]])
try:
    files = ["students.csv", "students2.csv"]
    with open("combined.csv", "w", newline="") as out:
        writer = csv.writer(out)
        for i, name in enumerate(files):
            with open(name, "r") as f:
                rows = list(csv.reader(f))
            writer.writerows(rows if i == 0 else rows[1:])   # header sirf ek baar
    print("Files combined into combined.csv")
except FileNotFoundError as e:
    print("Error:", e)
