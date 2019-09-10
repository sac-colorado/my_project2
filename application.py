import os

from flask import Flask, render_template, request, session
from flask_session import Session
# from flask_socketio import SocketIO, emit

app = Flask(__name__)
# app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.config["SECRET KEY"] = 'secret key'
# socketio = SocketIO(app)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

''' @app.route("/clearSession", methods=["GET", "POST"])
def clearSession():
    if session["display_name"] != Null:
        session.pop("display_name", None)
        return 'Session is cleared!' 
    return 'Session is already cleared' '''

@app.route("/login", methods=["GET", "POST"])
def login():
    display_name = request.form.get("name")
    if session.get("display_name") == None:    
        session["display_name"] = display_name # Save the display_name in the session dictionary
        return  "Welcome " + display_name + "!"
    else:
        if session.get("display_name") == display_name:
            return "Welcome back " + display_name + "!"
        
        return "You entered your display name incorrectly - please try again."
   

#if __name__ == '__main__':
#    socketio.run(app)