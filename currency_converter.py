# ---------- currency_converter.py ----------
import sqlite3

# Display all available currencies
conn = sqlite3.connect("currency.db")
cursor = conn.cursor()
cursor.execute("SELECT currency_code, rate_to_inr FROM exchange_rates")
rates = cursor.fetchall()
conn.close()

print(" Available Currencies:")
print("------------------------")
for code, rate in rates:
    print(f"{code}  ➜  1 {code} = {rate} INR")

# Take user input
from_currency = input("\nEnter currency code you want to convert FROM (e.g. USD): ").upper()
to_currency = input("Enter currency code you want to convert TO (e.g. EUR): ").upper()
amount = float(input("Enter amount: "))

# Connect again to get conversion rates
conn = sqlite3.connect("currency.db")
cursor = conn.cursor()

cursor.execute("SELECT rate_to_inr FROM exchange_rates WHERE currency_code=?", (from_currency,))
from_rate = cursor.fetchone()

cursor.execute("SELECT rate_to_inr FROM exchange_rates WHERE currency_code=?", (to_currency,))
to_rate = cursor.fetchone()
conn.close()

if from_rate and to_rate:
    # Convert: amount → INR → target currency
    in_inr = amount * from_rate[0]
    converted = in_inr / to_rate[0]
    print(f"\n💱 {amount:.2f} {from_currency} = {converted:.2f} {to_currency}")
else:
    print("\n Invalid currency code entered! Check the list and try again.")
