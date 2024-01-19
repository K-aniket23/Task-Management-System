import sqlite3
from manager import Manager
from database import Database_tables
from admin import Admin
from user import User

class TMS:
    def __init__(self):
        self.db_manager=Manager()
        self.table=Database_tables()
        self.admin_manager=Admin()
        self.user_manager=User()

        self.table.create_table()

        self.table.create_admin()

    def main(self):

        #UI

        print("Welcome to Task Manager")
        while True:
        
            print("Choose the Options")
            print("1 : Admin Login")
            print("2 : User Login")
            print("0 : Exit\n")

            choice=input("Enter any one option : ")

            if choice=="1":
                self.admin_login()
            elif choice=="2":
                self.user_login()
            elif choice=="0":
                print("Exiting the Task Manager\n")
                break
            else:
                print("Enter a valid option\n")
        
    #admin functions 

    def create_user(self):
        name=input("Enter the Name of User : ")
        username=input("Enter the Username : ")
        password=input("Enter the password : ")
        self.admin_manager.Create_new_user(name,username,password)

    def delete_user(self):
        user_id=input("Enter the UserID : ")
        self.admin_manager.Delete_user(user_id)

    def create_task(self):
        task_name=input("Enter the Task : ")
        task_description=input("Enter the Task Description : ")
        self.admin_manager.Create_task(task_name,task_description)

    def assign_task(self):
        print("Available Task to Assign : ")
        self.See_all_Tasks()
        print("Available User to Assign a Task : ")
        self.See_all_Users()
        taskid=input("Enter the Task ID : ")
        user_id=input("Enter the User ID to assign the task : ")
        self.admin_manager.Assign_task(taskid,user_id)

    def update_task(self):
        try:
            print("Available Task : ")
            self.See_all_Tasks()
            taskid=input("Enter the Task ID for updating the Task : ")
            task=self.admin_manager.find_task(taskid)
            if task:
                print("Set the Task Name : Choose the option")
                print("1 : Keep it same")
                print("2 : Set a New one\n")
                choice=input("Enter your Choice : ")
                if choice=='1':
                    task_name=task[0][1]
                elif choice=='2':
                    task_name=input("Enter the New Task : ")
                else:
                    print("Please Enter the Correct Option\n")
                
                print("Set the Task Description : Choose the option")
                print("1 : Keep it same")
                print("2 : Set a New one\n")
                choice=input("Enter your Choice : ")
                if choice=='1':
                    task_des=task[0][2]
                elif choice=='2':
                    task_des=input("Enter the New Description : ")
                else:
                    print("Please Enter the Correct Option\n")

                print("Set the Status : Choose the option")
                print("1 : Started")
                print("2 : In Progress- in mid way ")
                print("3 : Completed")
                print("4 : Not Complete\n")
                choice=input("Enter the New Status of the Task : ")
                if choice=='1':
                    task_status="Started"
                elif choice=='2':
                    task_status="In Progress"
                elif choice=='3':
                    task_status="Completed"
                elif choice=='4':
                    task_status="Not Complete"
                else:
                    print("Please Enter the Correct Option\n")
                
                print("Set the User whom to assign this task : Choose the option")
                print("1 : Keep it same")
                print("2 : Set a New one\n")
                choice=input("Enter your Choice : ")
                if choice=='1':
                    uid=task[0][5]
                elif choice=='2':
                    uid=input("Enter the New User whom to assign this task : ")
                else:
                    print("Please Enter the Correct Option\n")
                self.admin_manager.Update_task(task_name,task_des,task_status,uid,taskid)
            else:
                print("Please Enter a Valid Task ID\n")
        except Exception as e:
            print(f"Something Went Wrong : Reason : {e}\n")

    def delete_task(self):
        taskid=input("Enter the Task ID to Delete : ")
        if taskid=='0':
            print("Please Enter a Valid TaskID")
        else:
            self.admin_manager.detete_task(taskid)
        
    def See_all_Users(self):
        print("These are the Available Users : ")
        self.admin_manager.See_all_users()

    def See_all_Tasks(self):
        print("These are the Available Tasks : ")
        self.admin_manager.See_all_tasks()
        
    #user functions
            
    def update_task_status(self,id):
        self.read_task(id)
        taskid=input("Enter the Task ID to Update : ")
        print(" ~~~~Set the New Status : ~~~~")
        print("1 : Started")
        print("2 : In Progress- in mid way ")
        print("3 : Completed\n")
        choice=input("Enter the New Status : ")
        if choice=='1':
            status="Started"
        elif choice=='2':
            status="In Progress"
        elif choice=='3':
            status="Completed"
        else:
            print("Please Enter the Correct Option\n")
        self.user_manager.Update_task_status(taskid,status,id)

    def read_task(self,id):
        print("Assigned Task : ")
        self.user_manager.Read_task(id)

    #admin menu

    def Admin_menu(self):
        while True:
            print("Enter the option ")
            print("1 : Create a New User")
            print("2 : Delete a Existing User")
            print("3 : Create a New Task")
            print("4 : Assign a Task to a User")
            print("5 : Update a Existing Task")
            print("6 : Delete a Existing Task")
            print("7 : See all the Available Users")
            print("8 : See all the Available Tasks")
            print("0 : Back to Home!\n")

            choice=input("Enter any one option : ")

            if choice=="1":
                self.create_user()
            elif choice=="2":
                self.delete_user()
            elif choice=="3":
                self.create_task()
            elif choice=="4":
                self.assign_task()
            elif choice=="5":
                self.update_task()
            elif choice=="6":
                self.delete_task()
            elif choice=="7":
                self.See_all_Users()
            elif choice=="8":
                self.See_all_Tasks()
            elif choice=="0":
                print("Logged Out\n")
                break
            else:
                print("Enter a valid option\n")

    def User_menu(self,id):
        while True: 
            print("Enter the option ")
            print("1 : Update the Status of your Task")
            print("2 : Read all your Assigned Tasks")
            print("0 : Back to Home!\n")

            choice=input("Enter any one option : ")

            if choice=="1":
                self.update_task_status(id)
            elif choice=="2":
                self.read_task(id)
            elif choice=="0":
                print("Logged Out\n")
                break
            else:
                print("Enter a valid option\n")

        #login options

    def admin_login(self):
        try:
            username=input("Enter the Username : ")
            password=input("Enter the Password : ")
            u,p=self.admin_manager.Admin_Login(username,password)
            if u==username and p==password:
                print("Admin Login Successfully\n")
                self.Admin_menu()
        except TypeError:
            print("Please Enter a Valid Username and Password\n")


    def user_login(self):
        try:
            username=input("Enter the Username : ")
            password=input("Enter the Password : ")
            u,p,id=self.user_manager.Login_user(username,password)
            if (u,p,id) is not None:
                print(f"User Login Successfully with id : {id}\n")
                self.user_manager.Notification(str(id))
                self.User_menu(str(id))
            else:
                print("Please Enter a Valid Username and Password\n")
        except TypeError:
            print(f"Please Enter a Valid Username and Password\n")

        
    
if __name__ == '__main__':
    app=TMS()
    app.main()
    app.db_manager.close_connection()
        

        