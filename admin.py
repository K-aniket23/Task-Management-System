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
        if admin_data:

            u=admin_data[0][2]
            p=admin_data[0][3]
            return u,p
        else:
            print("Enter the Correct Username and Password")
        
    def Create_new_user(self,name,username,password):
        #insert a new user in the employee table
        self.db_manager.execute_command("""INSERT INTO EMPLOYEE(name, username, password) 
                                   VALUES (?,?,?)""",(name,username,password))
        print(f"User Named {name} Created Successfully!")

    def Delete_user(self,user_id):
        #insert a new user in the employee table
        self.db_manager.execute_command("""DELETE FROM EMPLOYEE
                                        WHERE userid=?""",(user_id))
        print(f"User Deleted Successfully") 

    def Create_task(self,task_name,task_description):
        #insert a new task in the task table
        self.db_manager.execute_command("""INSERT INTO TASK(task_name, task_description, task_status, task_seen)
                                       VALUES(?,?,'Not Complete','1')""", (task_name,task_description)) 
        print(f"Task {task_name} Created Successfully") 
        
    def Assign_task(self,task_id,userid):
        self.db_manager.execute_command("""UPDATE TASK
                                        SET UserID=?
                                        WHERE taskid=?""", (userid,task_id))
        print(f"Task {task_id} Assigned Successfully to User : {userid}") 


    def Update_task(self,task_name,task_des,task_status,uid,taskid):
        self.db_manager.execute_command("""UPDATE TASK 
                                        SET task_name = ?,
                                        task_description=?,
                                        task_status =?,
                                        UserID =?
                                        WHERE taskid=?
                                        """, (task_name,task_des,task_status,uid,taskid))
        print(f"Task {task_name} Updated Successfully") 
        
    def detete_task(self,taskid):
        self.db_manager.execute_command("""DELETE FROM TASK
                                        WHERE taskid=?""",(taskid))
        print(f"Task Deleted Successfully") 

    def See_all_users(self):
        users= self.db_manager.print_output("""SELECT * FROM EMPLOYEE""")
        for user in users:
            uid=str(user[0])
            tasks=self.db_manager.print_output("""SELECT * FROM TASK WHERE UserID = ?""",(uid))
            i=1
            task_assigned=False
            for task in tasks:  
                if str(task[5])==uid:
                    if not task_assigned:
                        print(f"User ID : {user[0]} | Name : {user[1]} | Username : {user[2]} | Password : {user[3]} | Assigned Tasks : ")
                        task_assigned=True
                    print(f"  | {i} :- Task ID : {task[0]} | Task Name: {task[1]} | Task Description: {task[2]} | Task Status: {task[3]}")
                    i+=1
            if not task_assigned:
                    
                print(f"User ID : {user[0]} | Name : {user[1]} | Username : {user[2]} | Password : {user[3]} | Assigned Tasks : No Task Assigned Yet")
            print()
        print()

    def See_all_tasks(self):
        tasks=self.db_manager.print_output("""SELECT * FROM TASK""")
        for task in tasks:
            print(f"Task ID: {task[0]} | Task Name: {task[1]} | Task Description: {task[2]} | Task Status: {task[3]} | Assigned to User with User ID: {task[5] if task[5] is not None else 'None'}")
        print()
