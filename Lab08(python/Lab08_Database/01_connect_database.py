# Program 1: Connect to a database and display a success message
# SQLite use kiya hai (built-in). MySQL ke liye: mysql.connector.connect(host="localhost", user="root", password="...", database="student_db")
import sqlite3
conn = None
try:
    conn = sqlite3.connect("student_db.db")
    print("Connected to database successfully!")
except sqlite3.Error as e:
    print("Connection failed:", e)
finally:
    if conn:
        conn.close()
