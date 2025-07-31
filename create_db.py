import sqlite3

conn = sqlite3.connect('iot_users.db')
c = conn.cursor()
c.execute('''CREATE TABLE users (username TEXT, password TEXT)''')
c.execute("INSERT INTO users VALUES ('admin', 'admin123')")  # Weak password
conn.commit()
conn.close()
print("Database created.")
