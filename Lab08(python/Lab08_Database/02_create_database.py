# Program 2: Create a new database
# SQLite me connect() file na ho to khud naya database bana deta hai.
# MySQL me: cursor.execute("CREATE DATABASE student_db")
import sqlite3, os
conn = None
try:
    conn = sqlite3.connect("student_db.db")
    print("Database 'student_db.db' created. File exists:", os.path.exists("student_db.db"))
except sqlite3.Error as e:
    print("Error:", e)
finally:
    if conn:
        conn.close()
