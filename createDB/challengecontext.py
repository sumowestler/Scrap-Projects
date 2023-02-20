import sqlite3

db = sqlite3.connect("contact.sqlite")

for name, phone, email in db.execute("SELECT * FROM contact, WHERE name = ?"):
    print(name)
    print(phone)
    print(email)
    print("*" * 20)