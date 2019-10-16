from app import app
from flask import render_template

# Set up routes
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Home")

@app.route("/login")
def login():
    return render_template("login.html",title="Login")

@app.route("/logout")
def logout():
    return render_template("logout.html", title="Logout")

