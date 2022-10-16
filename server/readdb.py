import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully")

cursor = conn.execute("SELECT location from locations")
for row in cursor:
   print(row[0])

conn.close()