import sqlite3 
from manager import Manager

class Database_tables:
    def __init__(self):
        self.db_manager=Manager()

    def create_table(self):
        # admin table ( id,name, username, password)
        self.db_manager.execute_command("""CREATE TABLE IF NOT EXISTS ADMIN(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        username TEXT UNIQUE NOT NULL, 
        password TEXT NOT NULL)""")

        # employee table (userid, name, username, password, task, task id, task_status)

        self.db_manager.execute_command("""CREATE TABLE IF NOT EXISTS EMPLOYEE(
            userid INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL);""")

        # task table (task id, task_name, task_status, userid)
        self.db_manager.execute_command("""CREATE TABLE IF NOT EXISTS TASK(
            taskid INTEGER PRIMARY KEY AUTOINCREMENT,
            task_name TEXT NOT NULL,
            task_description TEXT NOT NULL,
            task_status TEXT NOT NULL,
            task_seen INTEGER NOT NULL,
            UserID INTEGER REFERENCES EMPLOYEE(userid));""")

    def create_admin(self):
        admins = self.db_manager.print_output("SELECT * FROM ADMIN")

        if not admins:
            # If no admins exist, create the default admin
            self.db_manager.execute_command(
                """INSERT INTO ADMIN(name, username, password) VALUES ('Aniket', 'aniketk', 'abcd1234')"""
            )


        
        


