# ---------- view_database.py ----------
import sqlite3

# Connect to the database file
conn = sqlite3.connect("currency.db")
cursor = conn.cursor()

# Fetch all data from exchange_rates table
cursor.execute("SELECT * FROM exchange_rates")
rows = cursor.fetchall()

# Check if table has any data
if rows:
    print(" Currency Exchange Rates in Database:\n")
    print(f"{'ID':<5}{'Currency Code':<15}{'Rate to INR'}")
    print("-" * 35)
    for row in rows:
        print(f"{row[0]:<5}{row[1]:<15}{row[2]}")
else:
    print(" No data found in database! Please run create_database.py first.")

# Close connection
conn.close()
