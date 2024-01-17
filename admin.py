import sqlite3
from manager import Manager

# 1 make new user
# 2 assign task to user : see the list of user 
# see the task and then assign it
# 3 create task
# 4 see all task
# 5 see user
# 6 update the task

class Admin:
    def __init__(self):
        self.db_manager=Manager()

    def Admin_Login(self,Username,Password):
        admin_data=self.db_manager.print_output("""SELECT * FROM ADMIN 
                                          WHERE username=? AND password =?""",(Username,Password))
        return admin_data[2],admin_data[3]
        
    def Create_new_user(self,name,username,password):
        #insert a new user in the employee table
        self.db_manager.execute_command("""INSERT INTO EMPLOYEE(name, username, password) 
                                   VALUE (?,?,?)""",(name,username,password))
        print(f"User Named {name} Created Successfully!")

    def Delete_user(self,user_id):
        #insert a new user in the employee table
        self.db_manager.execute_command("""DELETE FROM EMPLOYEE
                                        WHERE userid=?""",(user_id))
        print(f"User Deleted Successfully") 

    def Create_task(self,task_name,task_description):
        #insert a new task in the task table
        self.db_manger.execute_command("""INSERT INTO TASK(task_name, task_description, task_status)
                                       VALUE(?,?,'Not Complete')""", (task_name,task_description)) 
        print(f"Task {task_name} Created Successfully") 
        
    def Assign_task(self,task_id,userid):
        self.db_manager.execute_command("""UPDATE TASK
                                        SET UserID=?,
                                        WHERE taskid=?""", (task_id,userid))
        print(f"Task {task_id} Assigned Successfully to User : {userid}") 

    def Update_task(self,task_name,task_status,taskid):
        print("Available Task : \n")
        self.See_all_tasks()
        self.db_manager.execute_command("""UPDATE TASK 
                                        SET task_name = ?,
                                        task_status =? 
                                        WHERE taskid=?
                                        """, (task_name,task_status,taskid))
        print(f"Task {task_name} Updated Successfully") 
        
    def detete_task(self,taskid):
        self.db_manager.execute_command("""DELETE FROM TASK
                                        WHERE taskid=?""",(taskid))
        print(f"Task Deleted Successfully") 

    def See_all_users(self):
        self.db_manager.print_output("""SELECT * FROM EMPLOYEE""")
        # for user in users:

    def See_all_tasks(self):
        self.db_manager.print_output("""SELECT * FROM TASK""")
