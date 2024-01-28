from flask import Flask, flash, redirect, render_template, request, session
from functools import wraps
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from cs50 import SQL  # Assuming you are using cs50 library for SQL

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
db = SQL("sqlite:///task.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

@app.route("/")
@login_required
def index():
    tasks = db.execute("SELECT * FROM DailyTasks WHERE user_id = ?", session["user_id"])
    return render_template('index.html', tasks=tasks)

@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()

    if request.method == "POST":
        if "login_button" in request.form:
            username = request.form.get("login_username")
            password = request.form.get("login_password")

            if not username or not password:
                error ="Must provide both username and password"
                return render_template("login.html",error=error)

            rows = db.execute(
                "SELECT * FROM users WHERE username = ?", username
            )

            # Ensure username exists and password is correct
            if len(rows) != 1 or not check_password_hash(
                rows[0]["password"], request.form.get("login_password")
            ):
                error ="Must provide correct username and password"
                return render_template("login.html" ,error=error)

            session["user_id"] = rows[0]["id"]
            return redirect("/")

        elif "sign_in_button" in request.form:
            name = request.form.get("sign_in_username")
            password = request.form.get("sign_in_password")
            confirmation = request.form.get("confirmation")

            if not name or not password:
                error =flash("Must provide both username and password for signup", "error")
                return render_template("login.html",error=error)

            if password != confirmation:
                error =flash("Password and confirmation do not match", "error")
                return render_template("login.html",error=error)

            names = db.execute("SELECT id  FROM users WHERE username =?" ,name)
            if names:
                error ="The username is already taken"
                return render_template("login.html",error=error)

            hashed_password = generate_password_hash(password)
            db.execute("INSERT INTO Users (username, password) VALUES (?, ?)", name, hashed_password)

            new_user = db.execute("SELECT * FROM Users WHERE username = ?", name)
            session["user_id"] = new_user[0]["id"]

            flash("Signup successful!", "success")
            return redirect("/")

    else:
        return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)


@app.route("/logout")
@login_required
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")
@app.route('/', methods=['POST'])
@login_required
def delete_task():
    task_id = request.form.get('delete_checkbox')

    if task_id and task_id.isdigit():
        task_id = int(task_id)
        db.execute("DELETE FROM DailyTasks WHERE task_id = :id", id=task_id)

    return index()

# Route to add a task
@app.route('/add_task', methods=['POST'])
@login_required
def add_task():
    taskname = request.form.get("Task_name")
    description = request.form.get("Task_Description")
    date = request.form.get("Due_Date")
    Priority = request.form["priority"]


    # Check for missing input
    if not taskname or not description or not date:
        error = "Fill in all the fields"
        return render_template("index.html", error=error)

    # Insert task into the database

    db.execute("INSERT INTO DailyTasks (user_id, task_name, task_description, due_date, priority) VALUES (?, ?, ?, ?, ?)",
                   session["user_id"], taskname, description, date, Priority)

    return redirect("/")



