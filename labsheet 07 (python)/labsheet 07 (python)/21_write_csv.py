# Program 21: Create and write data into a CSV file
import csv
try:
    data = [["Name", "Age", "Marks"], ["Aman", 20, 85], ["Riya", 21, 92], ["Karan", 20, 38], ["Neha", 22, 76]]
    with open("students.csv", "w", newline="") as f:   # newline="" extra blank rows rokta hai
        writer = csv.writer(f)
        writer.writerows(data)
    print("CSV file created successfully.")
except IOError as e:
    print("Error:", e)
