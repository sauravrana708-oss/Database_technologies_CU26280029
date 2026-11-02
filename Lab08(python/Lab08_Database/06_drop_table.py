# Program 6: Drop (delete) a table
import sqlite3
conn = None
try:
    conn = sqlite3.connect("student_db.db")   # database se connect
    cur = conn.cursor()
    # Demo table banake drop karte hain taaki students table safe rahe
    cur.execute("CREATE TABLE IF NOT EXISTS old_records (id INTEGER)")
    cur.execute("DROP TABLE IF EXISTS old_records")
    conn.commit()
    print("Table 'old_records' dropped.")
except ValueError:
    print("Invalid input!")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if conn:
        conn.close()   # connection hamesha close karo
