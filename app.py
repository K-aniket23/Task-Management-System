import sqlite3
from manager import Manager
from database import DatabaseTables
from admin import Admin
from user import User


class TMS:
    def __init__(self):
        self.db_manager = Manager()
        self.table = DatabaseTables()
        self.admin_manager = Admin()
        self.user_manager = User()

        self.table.create_table()
        self.table.create_admin()

        self.menu_stack = []

    def main(self):
        print("Welcome to Task Manager")
        while True:
            print("Choose the Options")
            print("1: Admin Login")
            print("2: User Login")
            print("0: Exit\n")

            choice = input("Enter any one option: ")

            menu_options = {
                "1": self.admin_login,
                "2": self.user_login,
                "0": self.exit_program
            }

            menu_options.get(choice, self.invalid_option)()

    def admin_login(self):
        try:
            username = input("Enter the Username: ")
            password = input("Enter the Password: ")
            u, p = self.admin_manager.admin_login(username, password)
            if u == username and p == password:
                print("Admin Login Successfully\n")
                self.menu_stack.append(self.admin_menu)  
                self.admin_menu()
        except TypeError:
            print("Please Enter a Valid Username and Password\n")

    def user_login(self):
        try:
            username = input("Enter the Username: ")
            password = input("Enter the Password: ")
            u, p, id = self.user_manager.login_user(username, password)
            if (u, p, id) is not None:
                print(f"User Login Successfully with id: {id}\n")
                self.menu_stack.append(lambda: self.user_menu(str(id))) 
                self.user_manager.notification(str(id))
                self.user_menu(str(id))
            else:
                print("Please Enter a Valid Username and Password\n")
        except TypeError:
            print("Please Enter a Valid Username and Password\n")

    def admin_menu(self):
        while True:
            print("Enter the option ")
            print("1: Create a New User")
            print("2: Delete an Existing User")
            print("3: Create a New Task")
            print("4: Assign a Task to a User")
            print("5: Update an Existing Task")
            print("6: Delete an Existing Task")
            print("7: See all the Available Users")
            print("8: See all the Available Tasks")
            print("0: Back to Home!\n")

            choice = input("Enter any one option: ")

            menu_options = {
                "1": self.create_user,
                "2": self.delete_user,
                "3": self.create_task,
                "4": self.assign_task,
                "5": self.update_task,
                "6": self.delete_task,
                "7": self.see_all_users,
                "8": self.see_all_tasks,
                "0": self.back
            }

            menu_options.get(choice, self.invalid_option)()

    def user_menu(self, id):
        while True:
            print("Enter the option ")
            print("1: Update the Status of your Task")
            print("2: Read all your Assigned Tasks")
            print("0: Back to Home!\n")

            choice = input("Enter any one option: ")

            menu_options = {
                "1": lambda: self.update_task_status(id),
                "2": lambda: self.read_task(id),
                "0": self.back
            }

            menu_options.get(choice, self.invalid_option)()

    # Admin functions

    def create_user(self):
        name = input("Enter the Name of User: ")
        username = input("Enter the Username: ")
        password = input("Enter the password: ")
        self.admin_manager.create_new_user(name, username, password)

    def delete_user(self):
        user_id = input("Enter the UserID: ")
        self.admin_manager.delete_user(user_id)

    def create_task(self):
        task_name = input("Enter the Task: ")
        task_description = input("Enter the Task Description: ")
        self.admin_manager.create_task(task_name, task_description)

    def assign_task(self):
        print("Available Task to Assign: ")
        self.see_all_tasks()
        print("Available User to Assign a Task: ")
        self.see_all_users()
        task_id = input("Enter the Task ID: ")
        user_id = input("Enter the User ID to assign the task: ")
        self.admin_manager.assign_task(task_id, user_id)

    def update_task(self):
        try:
            print("Available Task: ")
            self.see_all_tasks()
            task_id = input("Enter the Task ID for updating the Task: ")
            task = self.admin_manager.find_task(task_id)
            if task:
                print("Set the Task Name: Choose the option")
                print("1: Keep it same")
                print("2: Set a New one\n")
                choice = input("Enter your Choice: ")
                task_name = task[0][1] if choice == '1' else input("Enter the New Task: ")

                print("Set the Task Description: Choose the option")
                print("1: Keep it same")
                print("2: Set a New one\n")
                choice = input("Enter your Choice: ")
                task_des = task[0][2] if choice == '1' else input("Enter the New Description: ")

                print("Set the Status: Choose the option")
                print("1: Started")
                print("2: In Progress- in mid way")
                print("3: Completed")
                print("4: Not Complete\n")
                choice = input("Enter the New Status of the Task: ")
                task_status = {
                    '1': 'Started',
                    '2': 'In Progress',
                    '3': 'Completed',
                    '4': 'Not Complete'
                }.get(choice, 'Not Complete')

                print("Set the User whom to assign this task: Choose the option")
                print("1: Keep it same")
                print("2: Set a New one\n")
                choice = input("Enter your Choice: ")
                uid = task[0][5] if choice == '1' else input("Enter the New User whom to assign this task: ")

                self.admin_manager.update_task(task_name, task_des, task_status, uid, task_id)
            else:
                print("Please Enter a Valid Task ID\n")
        except Exception as e:
            print(f"Something Went Wrong: Reason: {e}\n")

    def delete_task(self):
        task_id = input("Enter the Task ID to Delete: ")
        if task_id == '0':
            print("Please Enter a Valid TaskID")
        else:
            self.admin_manager.detete_task(task_id)

    def see_all_users(self):
        print("These are the Available Users: ")
        self.admin_manager.see_all_users()

    def see_all_tasks(self):
        print("These are the Available Tasks: ")
        self.admin_manager.see_all_tasks()

    # User functions

    def update_task_status(self, id):
        self.read_task(id)
        task_id = input("Enter the Task ID to Update: ")
        print(" ~~~~Set the New Status: ~~~~")
        print("1: Started")
        print("2: In Progress- in mid way")
        print("3: Completed\n")
        choice = input("Enter the New Status: ")
        task_status = {
            '1': 'Started',
            '2': 'In Progress',
            '3': 'Completed'
        }.get(choice, 'Not Complete')
        self.user_manager.update_task_status(task_id, task_status, id)

    def read_task(self, id):
        print("Assigned Task: ")
        self.user_manager.read_task(id)

    # Common menu options

    def invalid_option(self):
        print("Enter a valid option\n")

    def logout(self):
        print("Logged Out\n")

    def exit_program(self):
        print("Exiting the Task Manager\n")
        self.db_manager.close_connection()
        exit()

    def back(self):
        try:
            previous_menu = self.menu_stack.pop()  
            print("Going back\n")
            previous_menu()  
        except IndexError:
            print("Logged Out\n")
            self.main()  


if __name__ == '__main__':
    app = TMS()
    app.main()
