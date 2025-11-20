💱 Currency Converter (Python + SQLite)

A simple Python-based Currency Converter project that uses an SQLite database to store and retrieve exchange rates.
This project contains three main scripts:

create_database.py → Creates the database and inserts exchange rates

currency_converter.py → Converts from one currency to another

view_database.py → Displays all data stored in the database

📁 Project Structure
📂 Currency Converter Project
│
├── create_database.py
├── currency_converter.py
├── view_database.py
├── currency.db
└── README.md   (this file)

🚀 Features

✔ Stores exchange rates in a SQLite database
✔ Converts any supported currency → INR → target currency
✔ Prevents duplicate entries using INSERT OR IGNORE
✔ Displays all available currencies
✔ Easy to extend and add more currencies

🛠 Requirements

Python 3.x

SQLite3 (built-in with Python)

No external libraries required.

📌 How It Works
1️⃣ Create the Database

This script generates the database file currency.db
and inserts a list of predefined currency exchange rates.

Run:

python create_database.py


You should see:

Database created and data inserted successfully!

2️⃣ View All Stored Exchange Rates

Run:

python view_database.py


This displays all currency codes and their INR conversion rates.

3️⃣ Convert Currency

Run:

python currency_converter.py


Example:

Enter currency code you want to convert FROM (e.g. USD): INR
Enter currency code you want to convert TO (e.g. EUR): USD
Enter amount: 1000


If both currency codes exist in the database:

💱 1000.00 INR = 12.05 USD


If the currency code is wrong:

❌ Invalid currency code entered! Check the list and try again.

🔧 How Conversion Works (Formula)
amount_in_inr = amount * rate_of_from_currency
converted_amount = amount_in_inr / rate_of_to_currency


Example: Convert USD → EUR

1 USD = 83 INR
1 EUR = 90.5 INR

amount_in_inr = 1 * 83
converted = 83 / 90.5 = 0.917 EUR

📌 Adding More Currencies

Open create_database.py and add:

("XYZ", 123.45),


Then re-run:

python create_database.py

📜 License

This project is free to use for learning and academic purposes.
