# Program 27: Import data from a CSV file into a table
import sqlite3
conn = None
try:
    conn = sqlite3.connect("student_db.db")   # database se connect
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT NOT NULL, age INTEGER, marks INTEGER)")
    cur.execute("SELECT COUNT(*) FROM students")
    if cur.fetchone()[0] == 0:      # sample data sirf pehli baar
        cur.executemany("INSERT INTO students VALUES (?, ?, ?, ?)",
                        [(1, "Aman", 20, 85), (2, "Riya", 21, 92), (3, "Karan", 20, 38), (4, "Neha", 22, 76), (5, "Rohit", 21, 67)])
        conn.commit()
    import csv, os
    if not os.path.exists("students_import.csv"):   # demo file
        with open("students_import.csv", "w", newline="") as f:
            csv.writer(f).writerows([["name", "age", "marks"], ["Imported1", 22, 70], ["Imported2", 23, 88]])
    with open("students_import.csv", "r") as f:
        rows = [(r["name"], int(r["age"]), int(r["marks"])) for r in csv.DictReader(f)]
    cur.executemany("INSERT INTO students (name, age, marks) VALUES (?, ?, ?)", rows)
    conn.commit()
    print(len(rows), "records imported.")
except ValueError:
    print("Invalid input!")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if conn:
        conn.close()   # connection hamesha close karo
