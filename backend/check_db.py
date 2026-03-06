import sqlite3

try:
    conn = sqlite3.connect("security.db")
    cursor = conn.cursor()

    # List tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables:", tables)

    # Check columns of users table
    cursor.execute("PRAGMA table_info(users);")
    columns = cursor.fetchall()
    print("Columns in users:", columns)

    # Show all users
    cursor.execute("SELECT * FROM users;")
    users = cursor.fetchall()
    print("Users:", users)

except Exception as e:
    print("Error:", e)

finally:
    conn.close()
