import sqlite3
from manager import Manager

#read task
#set status
# may be using a variable i can track the last login and notification

class User:
    def __init__(self):
        self.db_manager=Manager()


    def Login_user(self,Username,Password):
        user_data=self.db_manager.print_output("""SELECT * FROM EMPLOYEE 
                                          WHERE username=? AND password =?""",(Username,Password))
        if user_data is not None:
            u=user_data[0][2]
            p=user_data[0][3]
            id=user_data[0][0]

            return u,p,id
        else:
            print("something went wrong")

    def Update_task_status(self,taskid,new_status,userid):
        user_data=self.db_manager.print_output('''SELECT * FROM TASK WHERE UserID=?''',(userid))
        task_arr = []  
        for task in user_data:
            print("Tasks Assigned to you : ")
            print(f"Task ID: {task[0]} | Task Name: {task[1]} | Task Description: {task[2]} | Task Status: {task[3]}")
            task_arr.append(str(task[0]))
        if taskid in task_arr:
            self.db_manager.execute_command("""UPDATE TASK
                                            SET task_status=?
                                            WHERE taskid=?""",(new_status,taskid)) 
            print(f"Task Updated Successfully") 
        else:
            print("Please Enter the Task that are asssigned to you!")
    
    def Read_task(self,Userid):
        tasks=self.db_manager.print_output("""SELECT * FROM TASK 
                                WHERE UserID=?""",(Userid))
        for task in tasks:
            if task[4]=='1':
                print(f"Task ID: {task[0]} | Task Name: {task[1]} | Task Description: {task[2]} | Task Status: {task[3]}  ~~~~ New Task")
            else:
                print(f"Task ID: {task[0]} | Task Name: {task[1]} | Task Description: {task[2]} | Task Status: {task[3]}")

        print()
        
    def Notification(self,userid):
        user_data=self.db_manager.print_output('''SELECT * FROM TASK WHERE UserID=?''',(userid))
        task_arr = []  
        for task in user_data:
            task_arr.append([str(task[0]), task[1], str(task[4])])

        if len(task_arr)==0:
            print("No Task Yet, Enjoy")

        for i in range(len(task_arr)):
            if task_arr[i][2]=='1':
                print(f"~~ Notification ~~ : You Got a Task Named : {task_arr[i][1]}, Task ID : {task_arr[i][0]}, Please check Your Task List")
                self.db_manager.execute_command("""UPDATE TASK
                                            SET task_seen=0
                                            WHERE taskid=?""",(task_arr[i][0]))
            else:
                print("No New Task Yet, You can Complete the already assigned tasks")
        


