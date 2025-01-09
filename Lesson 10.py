import sqlite3

connection = sqlite3.connect("ItStep_DB.sl3")
cur = connection.cursor()

cur.execute("CREATE TABLE first_table (name TEXT);")
print(connection)
print(cur)

connection.close()