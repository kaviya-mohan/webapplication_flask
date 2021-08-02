from flask import Blueprint,render_template,request,flash,redirect,url_for
from flask_mysqldb import MySQL
from . import createApp

auth = Blueprint("auth",__name__)
app = createApp()

mysql = MySQL(app)

@auth.route("login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        email = str(email)
        password = request.form.get('password')
        cursor = mysql.connection.cursor()
        cursor.execute("select * from login where email = %s", (email,) )
        records = cursor.fetchone()
        cursor.close()
        if not records:
            return "Email is not available. Please signup!"
        if records[2] == password:
            return "Login successful"
        else:
            return "Wrong password!"
    return render_template("login.html")

@auth.route("logout")
def logout():
    return "Logout page"

@auth.route("register", methods=["GET","POST"])
def signup():
    if request.method == "POST":
        email = request.form.get('email')
        firstName = request.form.get('uname')
        password = request.form.get('password')
        password1 = request.form.get('passwordd')
        if password != password1:
            return "password dont match!"
        if len(password) < 9:
            return "Password should be greater than 8"
        cursor = mysql.connection.cursor()
        cursor.execute('''INSERT into login VALUES (%s,%s,%s) ''', (email,firstName,password))
        mysql.connection.commit()
        cursor.close()
        return "Done!!"
    return render_template("register.html")
