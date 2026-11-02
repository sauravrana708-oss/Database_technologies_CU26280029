# Program 28: Display database errors using exception handling
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
    try:
        cur.execute("SELECT * FROM no_such_table")          # table exist nahi karti
    except sqlite3.OperationalError as e:
        print("OperationalError:", e)
    try:
        cur.execute("INSERT INTO students (id, name, age, marks) VALUES (1, 'Dup', 20, 50)")   # duplicate primary key
    except sqlite3.IntegrityError as e:
        print("IntegrityError:", e)
    try:
        cur.execute("SELEC * FROM students")                # syntax error
    except sqlite3.Error as e:
        print("General error:", e)
except ValueError:
    print("Invalid input!")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if conn:
        conn.close()   # connection hamesha close karo
