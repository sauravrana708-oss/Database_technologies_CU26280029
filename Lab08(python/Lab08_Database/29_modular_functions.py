# Program 29: Use functions to insert and fetch data (modular approach)
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

def insert_student(name, age, marks):
    return run("INSERT INTO students (name, age, marks) VALUES (?, ?, ?)", (name, age, marks))

def fetch_students():
    return run("SELECT * FROM students", fetch=True)

try:
    init_db()
    insert_student("Modular", 22, 80)
    for row in fetch_students():
        print(row)
except sqlite3.Error as e:
    print("Database error:", e)
