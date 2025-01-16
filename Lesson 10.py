import sqlite3

connection = sqlite3.connect("ItStep_DB.sl3")
cur = connection.cursor()

# cur.execute("CREATE TABLE first_table (name TEXT);")
# connection.commit()

cur.execute("INSERT INTO first_table (name) VALUES ('ivan');")
connection.commit()

cur.execute("SELECT rowid, name FROM first_table;")
connection.commit()

cur.execute("UPDATE first_table SET name = 'negr' WHERE rowid=1;")
connection.commit()

cur.execute("DELETE FROM first_table WHERE rowid = 2;")
connection.commit()

res = cur.fetchall()
print(res)

connection.close()