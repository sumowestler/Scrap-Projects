import sqlite3

db = sqlite3.connect("contact.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contact(name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contact(name, phone, email) VALUES('Tim', 12345, 'tim@anymail.com')")
db.execute("INSERT INTO contact VALUES('Brian',1234, 'brian@anymaile.com')")

cursor = db.cursor()    # Cursors are the way to query databases in python.
cursor.execute("SELECT * FROM contact")

# print(cursor.fetchall())    # Returns a list of tuples for items in the database.

print(cursor.fetchone())    # Fetchone returns one row then the next if used again.
print(cursor.fetchone())
print(cursor.fetchone())

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("*" * 20)

db.commit()     # Commit function commits the transaction to the database.
cursor.close()
db.close()
