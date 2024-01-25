import sqlite3
from manager import Manager
from user import User

class Notification:

    def __init__(self):
        self.db_manager=Manager()
        self.user_manager=User()

    def notification(self,userid):
        try:
            tasks=self.user_manager.task_data(userid)
            task_arr = []  
            for task in tasks:
                task_arr.append([str(task[0]), task[1], str(task[4])])

            check=0   
            for i in range(len(task_arr)):                   
                if task_arr[i][2]=='1':
                    print(f"~~ Notification ~~ : You Got a Task Named : {task_arr[i][1]}, Task ID : {task_arr[i][0]}, Please check Your Task List for More Detail\n")
                    self.db_manager.execute_command("""UPDATE TASK
                                                        SET task_seen=?
                                                        WHERE taskid=?""",(self.user_manager.taskSeen2,task_arr[i][0]))
                    check=1
                if check==0:
                    print(" ~~ No New Task Yet, You can Complete the already assigned tasks if any!\n")
                    check=1
                            
        except Exception as e:
            print(f"Something Went Wrong : Reason : {e}\n")