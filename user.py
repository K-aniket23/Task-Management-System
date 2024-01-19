import sqlite3
from manager import Manager

#read task
#set status
# may be using a variable i can track the last login and notification

class User:
    def __init__(self):
        self.db_manager=Manager()

    def task_data(self,userid):
        try:
            tasks=self.db_manager.print_output('''SELECT * FROM TASK WHERE UserID=?''',(userid))
            return tasks
        except Exception as e:
            print(f"Error, Please check userid Carefully : Reason : {e}\n")

    def Login_user(self,Username,Password):
        user_data=self.db_manager.print_output("""SELECT * FROM EMPLOYEE 
                                                WHERE username=? AND password =?""",(Username,Password))
        if user_data:
            u=user_data[0][2]
            p=user_data[0][3]
            id=user_data[0][0]

            return u,p,id
        else:
            print("something went wrong Please Check your ID and Password")

    def Update_task_status(self,taskid,new_status,userid):
        try:
            tasks=self.task_data([userid])
            task_arr = []  
            for task in tasks:
                task_arr.append(str(task[0]))
            if taskid in task_arr:
                self.db_manager.execute_command("""UPDATE TASK
                                                SET task_status=?
                                                WHERE taskid=?""",(new_status,taskid)) 
                print(f"Task Updated Successfully") 
            else:
                print("Please Enter the Task that are asssigned to you!")

        except Exception as e:
            print(f"Error, Please check taskid,new_status,userid details Carefully for update the task : Reason : {e}\n")
    
    def Read_task(self,Userid):
        try:
            tasks=self.task_data([Userid])
            for task in tasks:
                if task[4]==2:
                    print(f"Task ID: {task[0]} | Task Name: {task[1]} | Task Description: {task[2]} | Task Status: {task[3]}              ~~~~ New Task")
                    self.db_manager.execute_command("""UPDATE TASK
                                                SET task_seen=0
                                                WHERE taskid=?""",([str(task[0])]))

                else:
                    print(f"Task ID: {task[0]} | Task Name: {task[1]} | Task Description: {task[2]} | Task Status: {task[3]}")
            print()

        except Exception as e:
            print(f"Error, Please check userid Carefully to read all the Tasks: Reason : {e}\n")
        
    def Notification(self,userid):
        try:
            tasks=self.task_data([userid])
            task_arr = []  
            for task in tasks:
                task_arr.append([str(task[0]), task[1], str(task[4])])

            check=0   
            for i in range(len(task_arr)):
                    
                if task_arr[i][2]=='1':
                    print(f"~~ Notification ~~ : You Got a Task Named : {task_arr[i][1]}, Task ID : {task_arr[i][0]}, Please check Your Task List for More Detail\n")
                    self.db_manager.execute_command("""UPDATE TASK
                                                    SET task_seen=2
                                                    WHERE taskid=?""",([task_arr[i][0]]))
                    check=1
            if check==0:
                print(" ~~ No New Task Yet, You can Complete the already assigned tasks if any!\n")
                check=1
                        
        except Exception as e:
            print(f"Something Went Wrong : Reason : {e}\n")

                    
        


