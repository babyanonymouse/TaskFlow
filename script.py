# Dependencies
import time
import json
from datetime import datetime


# Load users data from file
def load_users():
    try:
        with open("user_database.json", "r") as file:
            data = file.read().strip()
            if not data:
                return {}
            return json.loads(data)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Database file not found. Creating a new one...")
        with open("user_database.json", "w") as file:
            json.dump({}, file)  # Create an empty JSON object
        return {}


# Load tasks data from file
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


# Save tasks data to file
def save_tasks():
    global task_database
    with open("tasks.json", "w") as file:
        json.dump(task_database, file, indent=4)


# Save user data to file
def save_users():
    global user_database
    with open("user_database.json", "w") as file:
        json.dump(user_database, file, indent=4)


# Initialize user and task databases
user_database = load_users()
task_database = load_tasks()


# Function to register a user
def register_user():
    print("\n <-- REGISTER -->")
    username = input("Enter a username: ").strip()
    if username in user_database:
        print("Username already exists! Try again.")
        return
    password = input("Enter your Password: ").strip()
    if len(password) < 6:
        print("Password can't be less than 6 characters!")
        return
    confirm_password = input("Confirm your password: ").strip()
    if confirm_password != password:
        print("Passwords don't match!")
        return
    user_database[username] = {"password": password}
    save_users()
    print("Registration Successful!")


# Function to log in user
def login_user():
    print("<-- LOGIN -->")
    username = input("Enter your username: ").strip()
    if username not in user_database:
        print("Username not found! Please register first.")
        return None
    password = input("Enter your password: ").strip()
    if user_database[username]["password"] == password:
        print(f"Welcome back, {username}!")
        return username
    else:
        print("Incorrect password. Please try again.")
        return None


# Function to view/modify profile
def view_profile(username):
    print("\n <-- VIEW PROFILE -->")
    print(f"Username: {username}")
    print("Do you want to modify your profile?: ")
    print("1. Change Username\n 2. Change Password\n 3. Exit\n")
    action_number = int(input("Enter the number of the action you want to perform: "))

    if action_number == 1:
        new_username = input("Enter new username: ").strip()
        if new_username in user_database:
            print("Username already exists! Try again.")
        else:
            user_database[new_username] = user_database.pop(username)
            save_users()
            print(f"Username changed to {new_username}!")
            return new_username  # return new username
    elif action_number == 2:
        new_password = input("Enter new password: ").strip()
        if len(new_password) < 6:
            print("Password can't be less than 6 characters!")
        else:
            confirm_password = input("Confirm your password: ").strip()
            if confirm_password != new_password:
                print("Passwords don't match!")
            else:
                user_database[username]["password"] = new_password
                save_users()
                print("Password changed successfully!")
    elif action_number == 3:
        print("Exiting profile management ...")
        return username  # return the same username
    else:
        print("Invalid action! Please choose '1', '2', or '3'.")
    return username  # return the same username


# Function to add a task
def add_task(username):
    if username not in task_database:
        task_database[username] = []

    print("\n<-- ADD TASK -->")
    title = input("Enter Task Title: ").strip()
    description = input("Enter Task Description: ").strip()

    # Prompt for due date with validation
    while True:
        due_date = input("Enter Due Date (YYYY-MM-DD): ").strip()
        try:
            due_date_obj = datetime.strptime(due_date, "%Y-%m-%d")
            if due_date_obj.date() < datetime.now().date():
                print("The date has already passed. Please enter a future date.")
            else:
                break
        except ValueError:
            print("Invalid date format! Please use YYYY-MM-DD.")

    priority = input("Enter priority (High/Medium/Low): ").strip().capitalize()
    status = (
        input("Enter status (Pending/In Progress/Completed): ").strip().capitalize()
    )

    # Create the task dictionary
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "priority": priority,
        "status": status,
    }

    # Add the task to the user's list
    task_database[username].append(task)
    save_tasks()
    print("Task added successfully!")


#  Function to view tasks
def view_task(username):
    print("\n <-- VIEW TASKS -->")
    tasks = task_database.get(username, [])
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, start=1):
        print(f"\nTask {idx}:")
        for key, value in task.items():
            print(f"{key.capitalize()}: {value}")
    print("\nEnd of tasks.\n")


# Function to delete a task
def delete_task(username):
    print("\n <-- DELETE TASK -->")
    tasks = task_database.get(username, [])
    if not tasks:
        print("No tasks found.")
        return

    view_task(username)
    try:
        task_index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            deleted_task = tasks.pop(task_index)
            save_tasks()
            print(f"Task '{deleted_task['title']}' successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Invalid input! Please enter a number.")


# Function to modify a specific task
def modify_task(username):
    if username not in task_database or not task_database[username]:
        print("No tasks found to modify.")
        return

    print("\n<-- MODIFY TASK -->")
    view_task(username)  # Display existing tasks for reference

    try:
        task_index = int(input("Enter the task number to modify: ")) - 1
        if task_index < 0 or task_index >= len(task_database[username]):
            print("Invalid task number. Please try again.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    task = task_database[username][task_index]
    print("\nSelected Task:")
    print(f"Title: {task['title']}")
    print(f"Description: {task['description']}")
    print(f"Due Date: {task['due_date']}")
    print(f"Priority: {task['priority']}")
    print(f"Status: {task['status']}")

    # Allow the user to modify specific fields
    print("\nEnter new values or press Enter to keep the current value.")
    title = input(f"Title [{task['title']}]: ").strip() or task["title"]
    description = (
        input(f"Description [{task['description']}]: ").strip() or task["description"]
    )
    # due_date = (
    #     input(f"Due Date (YYYY-MM-DD) [{task['due_date']}]: ").strip()
    #     or task["due_date"]
    # )
    # Prompt for due date with validation
    while True:
        try:
            due_date = (
                input(f"Due Date (YYYY-MM-DD) [{task['due_date']}]: ").strip()
                or task["due_date"]
            )
            due_date_obj = datetime.strptime(due_date, "%Y-%m-%d")
            if due_date_obj.date() < datetime.now().date():
                print("The date has already passed. Please enter a future date.")
            else:
                break
        except ValueError:
            print("Invalid date format! Please use YYYY-MM-DD.")
    priority = (
        input(f"Priority (High/Medium/Low) [{task['priority']}]: ").strip().capitalize()
        or task["priority"]
    )
    status = (
        input(f"Status (Pending/In Progress/Completed) [{task['status']}]: ")
        .strip()
        .capitalize()
        or task["status"]
    )

    # Update the task
    task_database[username][task_index] = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "priority": priority,
        "status": status,
    }

    save_tasks()
    print("Task updated successfully!")


# <=== MAIN PROGRAM LOOP ===> #
logged_in_user = None
while True:
    print("\n --- TaskFlow ---")
    time.sleep(0.5)
    print("Your Tasks, Your Flow, Your Success.")
    time.sleep(0.5)

    # show options based on user login status
    if not logged_in_user:
        action = input("Choose an action (register, login, exit): ").strip().lower()
        if action == "register":
            register_user()
        elif action == "login":
            logged_in_user = login_user()
        elif action == "exit":
            print("Exiting the system...")
            time.sleep(1)
            print("Bye")
            exit()
        else:
            print(
                "Invalid action! Please choose 'register', 'login', 'add', or 'exit'."
            )

    # show options for logged in user
    else:
        action = (
            input(
                "Choose an action for your tasks (add, view, delete, modify, profile, logout): "
            )
            .strip()
            .lower()
        )

        if action == "add":
            add_task(logged_in_user)
        elif action == "view":
            view_task(logged_in_user)
        elif action == "delete":
            delete_task(logged_in_user)
        elif action == "modify":
            modify_task(logged_in_user)
        elif action == "profile":
            logged_in_user = view_profile(logged_in_user)
        elif action == "logout":
            print(f"Logging out {logged_in_user}...")
            logged_in_user = None
        else:
            print(
                "Invalid action! Please choose 'add', 'view', 'delete', 'modify', or 'logout'."
            )