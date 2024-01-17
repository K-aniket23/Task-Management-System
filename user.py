import sqlite3
from manager import Manager

#read task
#set status
# may be using a variable i can track the last login and notification

class User:
    def __init__(self,db_manager):
        self.db_manager=db_manager

    def Login_user(self,Username,Password):
        user_data=self.db_manager.print_output("""SELECT * FROM EMPLOYEE 
                                          WHERE username=? AND password =?""",(Username,Password))
        return user_data[2],user_data[3],user_data[0]

    def Update_task_status(self,taskid,new_status,userid):
        user_data=self.db_manager.print_output('''SELECT * FROM TASK WHERE UserID=?'''(userid))
        task_arr = []  
        for row in user_data:
            task_arr.append(int(row[0]))  
        if taskid in task_arr:
            self.db_manager.execute_command("""UPDATE TASK
                                            SET task_status=?
                                            WHERE taskid=?""",(new_status,taskid)) 
            print(f"Task Updated Successfully") 
        else:
            print("Please Enter the Task that are asssigned to you!")
    
    def Read_task(self,Userid):
        self.db_manager.print_output("""SELECT * FROM TASK 
                                WHERE UserID=?""",(Userid))