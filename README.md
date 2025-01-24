# User Authentication and Task Management System

## Introduction

The User Authentication and Task Management System is a Python-based project developed during the RITA Africa Bootcamp. It offers functionalities for user registration, authentication, and task management, emphasizing user-friendly design and efficient data handling.

## Features

### User Management

- **Register**: New users can create an account by providing a username and password. Passwords must be at least 6 characters long.
- **Login**: Existing users can log in using their credentials.
- **Profile Management**:
  - View Profile: Displays the current username.
  - Change Username: Allows users to update their username.
  - Change Password: Users can securely update their password. Password validation ensures strong and matching passwords.

### Task Management

- **Add Task**: Users can add new tasks with the following attributes:
  - Title
  - Description
  - Due Date (validated to ensure it is not a past date)
  - Priority (High, Medium, Low)
  - Status (Pending, In Progress, Completed)
- **View Tasks**: Lists all tasks associated with the logged-in user.
- **Delete Task**: Users can remove specific tasks from their list.
- **Modify Task**: Allows users to update task details, including title, description, due date, priority, and status. The system ensures that modified due dates are not set in the past.

## How It Works

### For Non-Logged-In Users:

1. **Main Menu Options**:
   - `register`: Calls the `register_user()` function to create a new account.
   - `login`: Calls the `login_user()` function to authenticate an existing user.
   - `exit`: Exits the program.

### For Logged-In Users:

1. **Dashboard Options**:
   - `add`: Calls the `add_task()` function to create a new task.
   - `view`: Calls the `view_task()` function to display all tasks.
   - `delete`: Calls the `delete_task()` function to remove a task.
   - `modify`: Calls the `modify_task()` function to update task details.
   - `profile`: Calls the `view_profile()` function to view or update profile details.
   - `logout`: Logs the user out and returns them to the main menu.

## Data Management

- **User Data**:
  - Stored in `user_database.json`.
  - Includes username and password.
- **Task Data**:
  - Stored in `tasks.json`.
  - Includes task attributes such as title, description, due date, priority, and status.

## Security Features

- Password validation ensures strong and secure credentials.
- Users must confirm their current password before updating it.
- Task due dates are validated to prevent setting tasks in the past.

## Skills Demonstrated

- Nested menus for a dynamic user interface.
- Enhanced string manipulation for secure and efficient data handling.
- Control flow using loops and conditional statements.

## Conclusion

This project showcases essential features of a task management system while maintaining a strong focus on user experience and data integrity. It is a beginner-friendly implementation that highlights core programming concepts in Python.
