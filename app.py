import sqlite3

# Step 1: Create database and table
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS incidents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        website TEXT,
        attack_type TEXT,
        detected_time TEXT,
        recovery_status TEXT
    )
    """)

    conn.commit()
    conn.close()

# Step 2: Log a fake attack (simulation)
def log_attack():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO incidents (website, attack_type, detected_time, recovery_status)
    VALUES (?, ?, datetime('now'), ?)
    """, ("demo-website.com", "Website Defacement", "Recovered"))

    conn.commit()
    conn.close()

# Step 3: Display logs (proof)
def show_logs():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM incidents")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()

# Run all steps
init_db()
log_attack()
show_logs()


