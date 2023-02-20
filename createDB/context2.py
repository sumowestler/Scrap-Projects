import sqlite3

db = sqlite3.connect("contact.sqlite")

new_email = "newemail@update.com"
phone = input("Please enter a phone number")

# update_sql = "UPDATE contact SET email = '{}' WHERE phone = {}".format(new_email, phone)
update_sql = "UPDATE contact SET email = ? WHERE phone = ?"
update_cursor = db.cursor()
update_cursor.execute(update_sql, (new_email, phone))     # execute script is used for running more than one sql statement in one call.
print("{} was updated".format(update_cursor.rowcount))

print()
print("Are connections the same {}".format(update_cursor.connection == db))
print()

update_cursor.connection.commit()
update_cursor.close()

for name, phone, email in db.execute("SELECT * FROM contact"):
    print(name)
    print(phone)
    print(email)
    print("*" * 20)

db.close()
