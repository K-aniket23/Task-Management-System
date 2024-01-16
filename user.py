import sqlite3
from manager import Manager

#read task
#set status
# may be using a variable i can track the last login and notification

class User:
    def __init__(self,db_manager):
        self.db_manager=db_manager

    def Login(self,Username,Password):
        auth=self.db_manager.print_output("""SELECT * FROM EMPLOYEE 
                                          WHERE username=? AND password =?""",(Username,Password))
        if auth:
            print("Login Successfully")
        else:
            print("Invalid Username and Password")

    def Update_task(self,taskid,new_status):
        self.db_manager.execute_command("""UPDATE TASK
                                        SET task_status=?
                                        WHERE taskid=?""",(new_status,taskid)) 
        print(f"Task Updated Successfully") 
    
    def Read_task(self,Userid):
        self.db_manager.print_output("""SELECT * FROM TASK 
                                WHERE UserID=?""",(Userid))