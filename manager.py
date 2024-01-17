import sqlite3

class Manager:
    # db connect
    # cursor
    # execute comands
    # commit
    # close

    def __init__(self):
        self.Database= 'TMS.db'
        self.conn = sqlite3.connect(self.Database) #check if some error
        self.cursor = self.conn.cursor()

    # we should check for some parameters for executing the command
    def execute_command(self,query,param=None):
        if param:
            self.cursor.execute(query,param)
        else:
            self.cursor.execute(query)
        self.conn.commit()


    def print_output(self,query,param=None):
        if param:
            self.cursor.execute(query,param)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()


    def close_connection(self):
        self.conn.close()

    
    