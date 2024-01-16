import sqlite3

class Manager:
    # db connect
    # cursor
    # execute comands
    # commit
    # close

    def __init__(self):
        self.Database= 'TMS.db'
        self.conn = sqlite3.connect(self.Database) 
        self.cursor = self.conn.cursor()

    def execute_command(self,query):
        self.cursor.execute(query)
        return 
    
    def close_connection(self):
        self.conn.commit()
        self.conn.close()

    
    