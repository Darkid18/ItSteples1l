import sqlite3

connection = sqlite3.connect("ItStep_DB.sl3")
cur = connection.cursor()

# cur.execute("CREATE TABLE first_table (name TEXT);")
cur.execute("INSERT INTO first_table (name) VALUES ('ivan');")
print(connection)
print(cur)

connection.close()