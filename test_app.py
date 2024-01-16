import sqlite3 

conn = sqlite3.connect('TMS.db') 

cursor = conn.cursor()

Admin_Table ="""CREATE TABLE IF NOT EXISTS ADMIN(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    username TEXT UNIQUE NOT NULL, 
    password TEXT NOT NULL);"""
cursor.execute(Admin_Table)


cursor.execute('''INSERT INTO ADMIN VALUES ('1', 'Aniket', 'aniketk','abcd1234')''') 

# print("Data Inserted in the table: ") 
# data=cursor.execute('''SELECT * FROM ADMIN''') 
# for row in data: 
# 	print(row) 

# # Commit your changes in the database	 
# conn.commit() 

# # Closing the connection 
# conn.close()

# employee table (userid, name, username, password, task, task id, task_status)

employee_table="""CREATE TABLE IF NOT EXISTS EMP(
    userid INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    task_name TEXT,
    taskid INTEGER NOT NULL,
    task_status TEXT
);"""

# task table (task id, task_name, task_status, userid)
Task_table="""CREATE TABLE IF NOT EXISTS TASK(
    taskid INTEGER PRIMARY KEY AUTOINCREMENT,
    task_name TEXT NOT NULL
    task_status TEXT
);"""