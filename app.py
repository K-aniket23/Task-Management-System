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
        taskid=int(input("Enter the Task ID : "))
        user_id=int(input("Enter the User ID to assign the task : "))
        self.admin_manager.Assign_task(taskid,user_id)

    def update_task(self):
        print("Available Task : ")
        self.See_all_Tasks()
        taskid=int(input("Enter the Task ID for updating the Task : "))
        task_name=input("Enter the New Task : ")
        task_des=input("Enter the New Description : ")
        task_status=input("Enter the New Status of the Task : ")
        uid=int(input("Enter the New User whom to assign this task : "))
        self.admin_manager.Update_task(task_name,task_des,task_status,uid,taskid)

    def delete_task(self):
        taskid=input("Enter the Task ID to Delete : ")
        self.admin_manager.detete_task(taskid)
        
    def See_all_Users(self):
        print("These are the Available Users : ")
        self.admin_manager.See_all_users()

    def See_all_Tasks(self):
        print("These are the Available Tasks : ")
        self.admin_manager.See_all_tasks()
        
    #user functions
            
    def update_task_status(self,id):
        taskid=int(input("Enter the Task ID to Update : "))
        status=input("Enter the New Status of the Task : ")
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
        username=input("Enter the Username : ")
        password=input("Enter the Password : ")
        u,p=self.admin_manager.Admin_Login(username,password)
        if u==username and p==password:
            print("Admin Login Successfully\n")
            self.Admin_menu()
        else:
            print("Please Enter a Valid Username and Password\n")


    def user_login(self):
        username=input("Enter the Username : ")
        password=input("Enter the Password : ")
        u,p,id=self.user_manager.Login_user(username,password)
        if u==username and p==password:
            print("User Login Successfully\n")
            self.User_menu(id)
        else:
            print("Please Enter a Valid Username and Password\n")

        
        
    
if __name__ == '__main__':
    app=TMS()
    app.main()
    app.db_manager.close_connection()
        

        