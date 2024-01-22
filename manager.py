import sqlite3


class Manager:
    # db connect
    # cursor
    # execute comands
    # commit
    # close

    def __init__(self):
        self.database = 'TMS.db'
        try:
            self.conn = sqlite3.connect(self.database)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            raise ConnectionError(f"Error connecting to the database: {e}")

    def execute_command(self, query, param=None):
        try:
            if param:
                self.cursor.execute(query, param)
            else:
                self.cursor.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            self.conn.rollback()  
            raise RuntimeError(f"Error executing command: {e}")

    def print_output(self, query, param=None):
        try:
            if param:
                self.cursor.execute(query, param)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            raise RuntimeError(f"Error fetching data: {e}")

    def close_connection(self):
        try:
            self.conn.close()
        except sqlite3.Error as e:
            raise RuntimeError(f"Error closing connection: {e}")

    
    