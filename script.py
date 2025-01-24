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


# Function to add a task
def add_task(username):
    print("\n <-- ADD TASK -->")
    title = input("Enter Task Title: ").strip()
    description = input("Enter Task Description: ").strip()
    due_date = input("Enter Due Date (YYYY-MM-DD): ").strip()
    priority = input("Enter priority (High/Medium/Low): ").strip().capitalize()

    try:
        due_date_obj = datetime.strptime(due_date, "%Y-%m-%d")
        due_date = due_date_obj.strftime("%Y-%m-%d")
    except ValueError:
        print("Invalid date format! Task not added.")
        return

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "priority": priority,
        "status": "Pending",
    }

    if username not in task_database:
        task_database[username] = []
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


# Function to modify a task
def modify_task(username):
    print("\n <-- MODIFY TASK -->")
    tasks = task_database.get(username, [])
    if not tasks:
        print("No tasks found.")
        return

    view_task(username)
    try:
        task_index = int(input("Enter the task number to modify: ")) - 1
        if 0 <= task_index < len(tasks):
            task = tasks[task_index]
            print("Enter new task details. Leave blank to keep the same.")
            title = input(f"Enter Task Title ({task['title']}): ").strip()
            description = input(
                f"Enter Task Description ({task['description']}): "
            ).strip()
            due_date = input(f"Enter Due Date ({task['due_date']}): ").strip()
            priority = (
                input(f"Enter priority ({task['priority']}): ").strip().capitalize()
            )

            if title:
                task["title"] = title
            if description:
                task["description"] = description
            if due_date:
                try:
                    due_date_obj = datetime.strptime(due_date, "%Y-%m-%d")
                    task["due_date"] = due_date_obj.strftime("%Y-%m-%d")
                except ValueError:
                    print("Invalid date format! Task not modified.")
                    return
            if priority:
                task["priority"] = priority

            save_tasks()
            print(f"Task '{task['title']}' modified successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Invalid input! Please enter a number.")



# <=== MAIN PROGRAM LOOP ===> #
logged_in_user = None
while True:
    if not logged_in_user:
        print("\n --- TaskFlow ---")
        time.sleep(0.5)
        print("Your Tasks, Your Flow, Your Success.")
        time.sleep(0.5)
        print("Options: register, login, exit")
        action = input("Choose an action: ").strip().lower()
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
            print("Invalid action! Please choose 'register', 'login', 'add', or 'exit'.")
    else:
        print(f"Welcome, {logged_in_user}!")
        print("Options: add, view, delete, modify, logout")
        action = input("Choose an action: ").strip().lower()
        if action == "add":
            add_task(logged_in_user)
        elif action == "view":
            view_task(logged_in_user)
        elif action == "delete":
            delete_task(logged_in_user)
        elif action == "modify":
            modify_task(logged_in_user)
        elif action == "logout":
            print(f"Logging out {logged_in_user}...")
            logged_in_user = None
        else:
            print("Invalid action! Please choose 'add', 'view', 'delete', 'modify', or 'logout'.")
