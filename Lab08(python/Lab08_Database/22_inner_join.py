# Program 22: INNER JOIN between students and courses
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
    cur.execute("CREATE TABLE IF NOT EXISTS courses (course_id INTEGER PRIMARY KEY, course_name TEXT, student_id INTEGER, FOREIGN KEY (student_id) REFERENCES students(id))")
    cur.executemany("INSERT OR IGNORE INTO courses VALUES (?, ?, ?)",
                    [(101, "Python", 1), (102, "Java", 2), (103, "DBMS", 3), (104, "AI", 1)])
    conn.commit()
    cur.execute("""SELECT s.name, c.course_name
                   FROM students s INNER JOIN courses c ON s.id = c.student_id""")
    for name, course in cur.fetchall():
        print(f"{name:<10}{course}")
except ValueError:
    print("Invalid input!")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if conn:
        conn.close()   # connection hamesha close karo
