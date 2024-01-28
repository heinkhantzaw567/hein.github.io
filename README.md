# Daily Task Manager
    #### Video Demo:  <https://youtu.be/qilsjcHJ2fM?si=gc3i0uwuHpUq4Xfr>
    #### Description:
## Requirements

- Python 3.x
- Flask
- Flask-Session
- SQLite database
- cs50 library for SQL
- Werkzeug library for password hashing
## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/project/task-management-app.git
   cd task-management-app

Create a virtual environment:
    python -m venv venv
Activate the virtual environment:
On Windows:
    venv\Scripts\activate
On macOS and Linux:
    source venv/bin/activate
Install the required dependencies:
    Install the required dependencies:
    Create a SQLite database file:
    bash
    touch task.db
Set up the Flask application:
export FLASK_APP=app.py
export FLASK_ENV=development  # Optional for development mode

Run the application:
flask run

 Usage
Open your web browser and go to http://127.0.0.1:5000/.
Create a new account or log in if you already have one.
Add tasks using the "Add Task" form.
View and manage your tasks on the main page.
Log out when you are done.

Certainly! Below is the content for a single README file that includes the application's details, requirements, and installation instructions:

markdown
Copy code
# Task Management Web App

This web application allows users to manage their daily tasks. Users can log in, add tasks, view their task list, and delete tasks.

## Requirements

- Python 3.x
- Flask
- Flask-Session
- SQLite database
- cs50 library for SQL
- Werkzeug library for password hashing

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/task-management-app.git
   cd task-management-app
Create a virtual environment:

bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:

bash
Copy code
venv\Scripts\activate
On macOS and Linux:

bash
Copy code
source venv/bin/activate
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Create a SQLite database file:

bash
Copy code
touch task.db
Set up the Flask application:

bash
Copy code
export FLASK_APP=app.py
export FLASK_ENV=development  # Optional for development mode
Run the application:

bash
Copy code
flask run
The application should now be accessible at http://127.0.0.1:5000/.

Usage
Open your web browser and go to http://127.0.0.1:5000/.
Create a new account or log in if you already have one.
Add tasks using the "Add Task" form.
View and manage your tasks on the main page.
Log out when you are done.

Contributing
If you would like to contribute to the development of this application, please follow the steps below:

Fork the repository.
Create a new branch for your feature or bug fix: git checkout -b feature-name.
Commit your changes: git commit -m 'Add new feature'.
Push the branch to your fork: git push origin feature-name.
Create a pull request.


User-Friendly Interface:
The intuitive and user-friendly interface is designed to provide a seamless and efficient experience.
With a clean and organized layout, users can easily navigate through various sections and manage their tasks effortlessly.

Login and Sign-Up:
To access the features of the task management system, users need to log in or sign up.
If insufficient information is provided during the login or sign-up process, the program will automatically redirect the user to the login page with a clear error message, ensuring a smooth onboarding experience.

Task Entry and Organization:
Users can easily input tasks, categorize them, and provide essential details such as due dates, priorities, and descriptions.
This robust task entry system helps users keep their activities organized, making it easier to stay on top of their commitments.

Daily Overview:
A comprehensive daily overview feature allows users to see all their scheduled tasks and priorities at a glance.
This snapshot of the day's activities aids in effective time management and planning.

Task Prioritization:
The ability to prioritize tasks based on urgency and importance is a key feature.
Users can ensure they focus on the most critical tasks, helping them stay productive and meet deadlines efficiently.

Task Deletion:
Once a task is completed, users can easily delete it from the system.
The tasks are displayed in a table format for easy reference. There's also an option to delete tasks directly by clicking a checkbox within the table, streamlining the process of task management.

Logout Functionality:
For security and convenience, the interface includes a logout button.
Users can log out with a single click, ensuring that their task data is secure and that they have control over their account access.

Interactive Features:
The inclusion of checkboxes for task deletion adds an interactive element to the interface. This feature allows users to manage tasks in a more dynamic way, providing a sense of control and customization.

In summary, this task management system offers a well-rounded set of features, from user-friendly navigation to detailed task entry and prioritization.
The interactive elements and daily overview contribute to a productive and efficient task management experience, making it a valuable tool for users seeking to stay organized and focused.

