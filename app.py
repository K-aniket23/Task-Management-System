import sqlite3
from manager import Manager
from database import Database_tables
from admin import Admin
from user import User

class TMS:
    def __init__(self):
        self.db_manager=Manager
        self.database=Database_tables
        self.admin_manager=Admin
        self.user_manager=User

        self.database.create_table()

        self.database.create_admin()

    def main(self):
        

        