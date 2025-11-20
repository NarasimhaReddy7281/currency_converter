# ---------- create_database.py ----------
import sqlite3

conn = sqlite3.connect("currency.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS exchange_rates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    currency_code TEXT UNIQUE,
    rate_to_inr REAL
)
""")

exchange_rates = [
    ("USD", 83.0),    # US Dollar
    ("EUR", 90.5),    # Euro
    ("GBP", 104.2),   # British Pound
    ("JPY", 0.55),    # Japanese Yen
    ("AED", 22.6),    # UAE Dirham
    ("CAD", 60.2),    # Canadian Dollar
    ("AUD", 54.8),    # Australian Dollar
    ("CHF", 93.4),    # Swiss Franc
    ("CNY", 11.6),    # Chinese Yuan
    ("SGD", 61.3),    # Singapore Dollar
    ("ZAR", 4.3),     # South African Rand
    ("KRW", 0.064),   # South Korean Won
    ("THB", 2.3),     # Thai Baht
    ("NZD", 50.1),    # New Zealand Dollar
    ("RUB", 0.92)     # Russian Ruble
]

cursor.executemany(
    "INSERT OR IGNORE INTO exchange_rates (currency_code, rate_to_inr) VALUES (?, ?)",
    exchange_rates
)

conn.commit()
conn.close()

print(" Database created and data inserted successfully!")
