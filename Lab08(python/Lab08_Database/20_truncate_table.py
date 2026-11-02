# Program 20: Truncate a table keeping its structure
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
    # SQLite me TRUNCATE nahi hota, DELETE FROM use hota hai. (MySQL: TRUNCATE TABLE name)
    # Demo ke liye students ki copy par kaam kar rahe hain
    cur.execute("DROP TABLE IF EXISTS students_demo")
    cur.execute("CREATE TABLE students_demo AS SELECT * FROM students")
    cur.execute("DELETE FROM students_demo")
    conn.commit()
    cur.execute("SELECT COUNT(*) FROM students_demo")
    print("Rows after truncate:", cur.fetchone()[0])
    cur.execute("PRAGMA table_info(students_demo)")
    print("Structure intact, columns:", [c[1] for c in cur.fetchall()])
except ValueError:
    print("Invalid input!")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if conn:
        conn.close()   # connection hamesha close karo
