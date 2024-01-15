import sqlite3 

conn = sqlite3.connect('TMS.db') 

cursor = conn.cursor()

Admin_Table ="""CREATE TABLE ADMIN(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    username TEXT UNIQUE NOT NULL, 
    password TEXT NOT NULL);"""
cursor.execute(Admin_Table)


cursor.execute('''INSERT INTO ADMIN VALUES ('1', 'Aniket', 'aniketk','abcd1234')''') 

print("Data Inserted in the table: ") 
data=cursor.execute('''SELECT * FROM ADMIN''') 
for row in data: 
	print(row) 

# Commit your changes in the database	 
conn.commit() 

# Closing the connection 
conn.close()