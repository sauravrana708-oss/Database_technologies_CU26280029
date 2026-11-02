# Program 10: CRUD operations on a file
# Example I/O:
#   Menu: 1.Add 2.View 3.Modify 4.Delete 5.Exit

import os
FILE = "records.txt"                    # har line: roll,name,marks

def load():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return [line.strip().split(",") for line in f if line.strip()]

def save(records):
    with open(FILE, "w") as f:
        for r in records:
            f.write(",".join(r) + "\n")

while True:
    print("\n1. Add  2. View  3. Modify  4. Delete  5. Exit")
    choice = input("Enter choice: ")
    records = load()
    try:
        if choice == "1":
            records.append([input("Roll: "), input("Name: "), input("Marks: ")])
            save(records)
            print("Record added.")
        elif choice == "2":
            if not records:
                print("No records.")
            for r in records:
                print("Roll:", r[0], "| Name:", r[1], "| Marks:", r[2])
        elif choice == "3":
            roll = input("Roll to modify: ")
            for r in records:
                if r[0] == roll:
                    r[1], r[2] = input("New name: "), input("New marks: ")
                    save(records)
                    print("Record modified.")
                    break
            else:
                print("Roll not found.")
        elif choice == "4":
            roll = input("Roll to delete: ")
            new = [r for r in records if r[0] != roll]
            save(new)
            print("Record deleted." if len(new) < len(records) else "Roll not found.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
    except IOError as e:
        print("File error:", e)
