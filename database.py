import sqlite3

conn = sqlite3.connect("database.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY,
    balance REAL DEFAULT 0,
    referred_by INTEGER,
    referrals INTEGER DEFAULT 0,
    daily_bonus TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS withdraws(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    amount REAL,
    number TEXT,
    status TEXT DEFAULT 'Pending'
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS giftcodes(
    code TEXT PRIMARY KEY,
    amount REAL,
    used INTEGER DEFAULT 0
)
""")

conn.commit()
