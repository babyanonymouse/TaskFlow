# TaskFlow

## User Authentication and Task Management System

### Overview

This system allows users to register, log in, and manage tasks. After a successful login, the user can add, view, modify, or delete tasks.

### Features

1. **User Authentication**

   - Users can register by providing a username and password.
   - Users can log in with an existing username and password.

2. **Task Management**

   - Users can add tasks with a title, description, due date, and priority.
   - Users can view their tasks.
   - Users can modify existing tasks.
   - Users can delete tasks.

3. **File Persistence**
   - User data is stored in a file called `user_database.json`.
   - Task data is stored in a file called `tasks.json`.
   - The system automatically loads and saves data from/to these files.

### How It Works

#### Authentication Options

When the program starts, users are presented with the following options:

1. **`register`**: Registers a new user.

   - **Username**: The user's chosen username.
   - **Password**: The user's chosen password (must be at least 6 characters long).
   - **Password Confirmation**: Ensures the user has typed the password correctly.

2. **`login`**: Allows an existing user to log in.

   - **Username**: The user's registered username.
   - **Password**: The user's password.

3. **`exit`**: Exits the program.

#### Task Management Options (After Login)

Once logged in, the user will be able to manage their tasks with the following options:

1. **`add`**: Add a new task.

   - **Title**: The title of the task.
   - **Description**: A brief description of the task.
   - **Due Date**: The task's due date in `YYYY-MM-DD` format.
   - **Priority**: The task's priority (`High`, `Medium`, `Low`).

2. **`view`**: View all tasks assigned to the logged-in user.

3. **`delete`**: Delete a task by selecting the task number.

4. **`modify`**: Modify an existing task by selecting the task number and entering new details.

5. **`logout`**: Logs the user out, returning to the main menu.

---

### Instructions

1. **Run the Program:**

   - The program will prompt you to either `register`, `login`, or `exit`.
   - If you are logging in, you must have a previously registered account.

2. **If Logged In:**

   - You will be able to manage your tasks by selecting actions such as `add`, `view`, `delete`, `modify`, or `logout`.

3. **Files:**
   - The system will automatically save and load data from two files:
     - `user_database.json` - Stores user credentials.
     - `tasks.json` - Stores tasks for each user.

---

### Example Usage

```bash
Welcome to TaskFlow!

Choose an action: register

Enter a username: john_doe
Enter your Password: my_password
Confirm your password: my_password
Registration Successful!

Choose an action: login

Enter your username: john_doe
Enter your password: my_password
Welcome back, john_doe!

Choose an action: add
Enter Task Title: Learn Python
Enter Task Description: Complete Python tutorial
Enter Due Date (YYYY-MM-DD): 2025-02-01
Enter priority (High/Medium/Low): High
Task added successfully!

Choose an action: view
Task 1:
Title: Learn Python
Description: Complete Python tutorial
Due Date: 2025-02-01
Priority: High
Status: Pending

Choose an action: logout
Logging out john_doe...
```

---

### File Structure

- **`user_database.json`**: Stores user credentials (username and password).
- **`tasks.json`**: Stores tasks for each user, including title, description, due date, priority, and status.

---

### Notes:

- If the `user_database.json` or `tasks.json` files do not exist, they will be created automatically when the program is run.
- The program checks for valid inputs, such as password length and due date format, to ensure consistency.
