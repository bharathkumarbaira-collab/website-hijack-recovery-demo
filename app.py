import sqlite3
from datetime import datetime

print("App started successfully")

# Create / connect database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS incidents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    website TEXT,
    attack_type TEXT,
    time TEXT,
    status TEXT
)
""")

# Insert demo attack
cursor.execute("""
INSERT INTO incidents (website, attack_type, time, status)
VALUES (?, ?, ?, ?)
""", (
    "demo-website.com",
    "Website Defacement",
    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "Recovered"
))

conn.commit()

# Fetch logs
cursor.execute("SELECT * FROM incidents")
rows = cursor.fetchall()

print("---- INCIDENT LOGS ----")
for row in rows:
    print(row)

conn.close()
print("App finished")




