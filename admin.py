import sqlite3
from manager import Manager
from user import User

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
        self.user_manager=User()

    def find_user(self,uid):
        try:
            user= self.db_manager.print_output("""SELECT * FROM EMPLOYEE WHERE userid=?""",([uid]))
            return user
        except Exception as e:
            print(f"Something Went Wrong in finding user : Reason : {e}\n")
        
    def find_task(self,tid):
        try:
            task= self.db_manager.print_output("""SELECT * FROM TASK WHERE taskid=?""",([tid]))
            return task
        except Exception as e:
                print(f"Something Went Wrong in finding task : Reason : {e}\n")
    
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
        try:
            self.db_manager.execute_command("""INSERT INTO EMPLOYEE(name, username, password) 
                                    VALUES (?,?,?)""",(name,username,password))
            print(f"User Named {name} Created Successfully!\n")
        except sqlite3.IntegrityError:
            print(f"Error, Username is Already Taken, Please Use Different Username\n")
    
    def Delete_user(self,user_id):
        try:
            user=self.find_user(user_id)
            if user:
                self.db_manager.execute_command("""UPDATE TASK
                                                            SET task_seen=1,
                                                                UserID=NULL
                                                            WHERE UserID=?""",([user_id]))
                self.db_manager.execute_command("""DELETE FROM EMPLOYEE
                                                    WHERE userid=?""",([user_id]))
            else:
                print(f"User Deleted Successfully\n")   
            print("Error, Please Enter The Correct User ID\n")

        except Exception as e:
            print(f"Something Went Wrong : Reason : {e}\n")   

    def Create_task(self,task_name,task_description):
        #insert a new task in the task table
        try:
            self.db_manager.execute_command("""INSERT INTO TASK(task_name, task_description, task_status, task_seen)
                                        VALUES(?,?,'Not Complete','1')""", (task_name,task_description)) 
            print(f"Task {task_name} Created Successfully\n") 
        except Exception as e:
            print(f"Something Went Wrong : Reason : {e}\n") 

        
    def Assign_task(self,task_id,userid):
        # try:
            task=self.find_task(task_id)
            user= self.find_user(userid)
            if task and user:
                if task[0][4]==1:
                    pass
                else:
                    self.db_manager.execute_command("""UPDATE TASK
                                                    SET task_seen=1
                                                    WHERE taskid=?""",([task_id]))

                self.db_manager.execute_command("""UPDATE TASK
                                                SET UserID=?
                                                WHERE taskid=?""", (userid,task_id))
                print(f"Task {task_id} Assigned Successfully to User : {userid}\n") 
            else:
                print("Please Enter a Valid User ID or Task ID\n")
        # except Exception as e:
        #     print(f"Something Went Wrong : Reason : {e}\n")

    def Update_task(self,task_name,task_des,task_status,uid,taskid):
        # try:
            task=self.find_task(taskid)
            if task:
                self.db_manager.execute_command("""UPDATE TASK 
                                                SET task_name = ?,
                                                task_description=?,
                                                task_status =?,
                                                task_seen=1,
                                                UserID =?
                                                WHERE taskid=?
                                                """, (task_name,task_des,task_status,uid,taskid))
                print(f"Task {task_name} Updated Successfully\n") 
            else:
                print("Please Enter a Valid Task ID")
        # except Exception as e:
        #     print(f"Something Went Wrong : Reason : {e}\n")
        
    def detete_task(self,taskid):
        try:
            task=self.find_task(taskid)
            if task:
                self.db_manager.execute_command("""DELETE FROM TASK
                                                    WHERE taskid=?""",([taskid]))
                print(f"Task Deleted Successfully\n") 
            else:
                print("Please Enter a Valid Task ID\n")
        except Exception as e:
            print(f"Something Went Wrong : Reason : {e}\n")

    def See_all_users(self):
        try:
            users= self.db_manager.print_output("""SELECT * FROM EMPLOYEE""")
            for user in users:
                uid=str(user[0])
                tasks=self.db_manager.print_output("""SELECT * FROM TASK WHERE UserID = ?""",([uid]))
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
        except Exception as e:
            print(f"Something Went Wrong : Reason : {e}\n")
        

    def See_all_tasks(self):
        try:
            tasks=self.db_manager.print_output("""SELECT * FROM TASK""")
            for task in tasks:
                print(f"Task ID: {task[0]} | Task Name: {task[1]} | Task Description: {task[2]} | Task Status: {task[3]} | Assigned to User with User ID: {task[5] if task[5] is not None else 'None'}")
            print()
        except Exception as e:
            print(f"Something Went Wrong : Reason : {e}\n")
