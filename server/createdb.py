import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully")

conn.execute('DROP TABLE locations')
conn.execute('CREATE TABLE locations (location TEXT)')
conn.commit()

print("Table created successfully")
conn.close()