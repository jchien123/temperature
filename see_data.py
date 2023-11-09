import sqlite3

conn = sqlite3.connect("temp_data.sqlite")
c = conn.cursor()

x = c.execute("SELECT * FROM temp").fetchall()
print(x)

conn.close()
