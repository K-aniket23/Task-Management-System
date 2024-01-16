import sqlite3 
from manager import Manager

class Database_tables:
    def __init__(self,db_manager):
        self.db_manager=db_manager

    def create_table(self):
        # admin table ( id,name, username, password)
        self.db_manager.execute_command("""CREATE TABLE IF NOT EXISTS ADMIN(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        username TEXT UNIQUE NOT NULL, 
        password TEXT NOT NULL);""")

        # employee table (userid, name, username, password, task, task id, task_status)

        self.db_manager.execute_command("""CREATE TABLE IF NOT EXISTS EMPLOYEE(
            userid INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
        );""")

        # task table (task id, task_name, task_status, userid)
        self.db_manager.execute_command("""CREATE TABLE IF NOT EXISTS TASK(
            taskid INTEGER PRIMARY KEY AUTOINCREMENT,
            task_name TEXT NOT NULL,
            task_description TEXT NOT NULL,
            task_status TEXT NOT NULL,
            UserID INTEGER REFERENCES EMPLOYEE(userid)
        );""")

        print("Tables Created or Already exist")

