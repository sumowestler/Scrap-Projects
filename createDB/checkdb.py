import sqlite3

comm = sqlite3.connect("contact.sqlite")
comm_cursor = comm.cursor()
name = input("Please select a name")
select_name = "SELECT * FROM contact WHERE name = ?"    #The question mark can be used in order to substitute

for row in comm_cursor.execute(select_name, (name,)):
    print(row)
comm_cursor.close()
comm.close()