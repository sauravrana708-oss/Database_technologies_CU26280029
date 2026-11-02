# Program 5: List all tables in the database
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
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")   # MySQL me: SHOW TABLES
    for t in cur.fetchall():
        print(t[0])
except ValueError:
    print("Invalid input!")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if conn:
        conn.close()   # connection hamesha close karo
