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

# Global storage for chat room --> users, channels, messages
user_names = []
channel_list = [tst_channel1, tst_channel2, tst_channel3]
users_and_messages = {}


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", error_message = "")

@app.route("/login", methods=["GET", "POST"])
def login():
    display_name = request.form.get("name")
    if session.get("display_name") == None:    # Check if display_name is already in the sessions dictionary
        session["display_name"] = display_name # Save the display_name in the session dictionary
        welcome_str = "Welcome " + display_name + "!"
        user_names.append(display_name)        # Add the new display_name to the user_names list.
        string_names = str(user_names)
        return render_template("channels_page.html", welcome_message = welcome_str + '  ' + string_names)
        #return  render_template("channel_list.html", channels = channel_list, welcome = welcome_str)
    else:
        if session.get("display_name") == display_name:
            welcome_str = "Welcome back " + display_name + "!"
            string_names = str(user_names)
            return render_template("channels_page.html", welcome_message = welcome_str + '  ' + string_names)
            #return  render_template("channel_list.html", channels = channel_list, welcome = welcome_str)
                  
        return render_template("index.html" , error_message = "You entered your 'saved' display name incorrectly - please try again")

@app.route("/list_current_channels", methods=["GET"])
def list_current_channels():
    return render_template("list_current_channels.html", channel_list = "channel_list")

@app.route("/create_new_channel", methods=["GET", "POST"])
def create_new_channel():
    return render_template("create_new_channel.html")


#if __name__ == '__main__':
#    socketio.run(app)