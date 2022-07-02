import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully.")

conn.execute('''CREATE TABLE participants
    (id INTEGER PRIMARY KEY NOT NULL, 
    fname TEXT NOT NULL, 
    lname TEXT NOT NULL, 
    phone TEXT NOT NULL, 
    email TEXT NOT NULL, 
    address TEXT NOT NULL)''')
print('Table created successfully.')
conn.close()