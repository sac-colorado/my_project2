import os

from flask import Flask, render_template, request, session
from flask_session import Session
# from flask_socketio import SocketIO, emit

app = Flask(__name__)
# app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.config["SECRET KEY"] = os.urandom(24)
# socketio = SocketIO(app)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    display_name = request.form.get("name")
    if session.get("display_name") == None:    # Check if display_name is already in the sessions dictionary
        session["display_name"] = display_name # Save the display_name in the session dictionary
        return  "Welcome " + display_name + "!"
    else:
        if session.get("display_name") == display_name:
            return "Welcome back " + display_name + "!"
        
        return "You entered your display name incorrectly - please try again."
   

#if __name__ == '__main__':
#    socketio.run(app)