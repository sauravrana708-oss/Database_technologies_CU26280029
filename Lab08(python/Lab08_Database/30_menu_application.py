# Program 30: Menu-driven student management application (Add, View, Update, Delete)
import sqlite3
DB = "student_db.db"

def run(query, params=(), fetch=False):
    # Ek helper: connection kholo, query chalao, commit karo, connection band karo
    conn = sqlite3.connect(DB)
    try:
        cur = conn.cursor()
        cur.execute(query, params)          # ? placeholders = SQL injection se bachav
        rows = cur.fetchall() if fetch else None
        conn.commit()
        return rows if fetch else cur.rowcount
    finally:
        conn.close()

def init_db():
    run("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT NOT NULL, age INTEGER, marks INTEGER)")
    if run("SELECT COUNT(*) FROM students", fetch=True)[0][0] == 0:
        for s in [(1, "Aman", 20, 85), (2, "Riya", 21, 92), (3, "Karan", 20, 38)]:
            run("INSERT INTO students VALUES (?, ?, ?, ?)", s)

def add_student():
    name = input("Name: ")
    age = int(input("Age: "))
    marks = int(input("Marks: "))
    run("INSERT INTO students (name, age, marks) VALUES (?, ?, ?)", (name, age, marks))
    print("Student added.")

def view_students():
    rows = run("SELECT * FROM students", fetch=True)
    if not rows:
        print("No records.")
    for r in rows:
        print(f"ID: {r[0]} | Name: {r[1]} | Age: {r[2]} | Marks: {r[3]}")

def update_student():
    sid = int(input("Student ID to update: "))
    marks = int(input("New marks: "))
    print("Updated." if run("UPDATE students SET marks = ? WHERE id = ?", (marks, sid)) else "ID not found.")

def delete_student():
    sid = int(input("Student ID to delete: "))
    print("Deleted." if run("DELETE FROM students WHERE id = ?", (sid,)) else "ID not found.")

def main():
    init_db()
    while True:
        print("\n--- Student Management ---")
        print("1. Add  2. View  3. Update  4. Delete  5. Exit")
        choice = input("Enter choice: ")
        try:
            if choice == "1": add_student()
            elif choice == "2": view_students()
            elif choice == "3": update_student()
            elif choice == "4": delete_student()
            elif choice == "5":
                print("Goodbye!")
                break
            else: print("Invalid choice.")
        except ValueError:
            print("Invalid input, please enter numbers where required.")
        except sqlite3.Error as e:
            print("Database error:", e)

main()
