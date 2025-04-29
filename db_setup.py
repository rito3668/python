import sqlite3
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Setup DB
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL
)
''')

# Insert initial users
users = {
    "john": "pass123",
    "alice": "secure456"
}

for username, password in users.items():
    hashed = hash_password(password)
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed))
    except sqlite3.IntegrityError:
        continue  # User already exists

conn.commit()
conn.close()
print("Database initialized with users.")
