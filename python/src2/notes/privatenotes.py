from flask import Flask, render_template, request, session
from flask_session import Session
Session(app)
#make session private, Session(app)
#allows notes to be permanently stored for an individual. The flask recognizes the user's sessions
#so when a user exits the browser and comes back later it can figure out who that user is by their
#browser opening. Somehow the person is identified in some way from this and the flask
#recogonizes that returning user when they open a new browser window and gets their
#session notes and displays them without the notes being lost.
#I will have to check to see if flask run ends if the data persists.
#cookies in the browser when reopened is used to redisplay the notes.
#flask website has these features and examples.
#https://flask.palletsprojects.com/en/1.1.x/
app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# this notes = [] declaration is no longer needed. It's the global notes passed across all sessions
# and stores notes from all different sessions in one note but when the flask server exits 
# the data is lost and the notes are all gone because the notes in this variable are not stored.
# The data persists as long as flask run is continuing to run. Once the flask run is cancelled
# the notes = [] data is lost.

@app.route("/", methods=["GET", "POST"])
def index():
    if session.get("notes") is None: 
        session["notes"] == []
    #if session["notes] does not exist then create an empty dictionary sessions with index notes

    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)
        #sessions["notes"] is a dictionary specific to the user
        #ONLY append note to individual session

        #session["notes"].append(note) gives access to just one session the notes making notes private

    return render_template("index.html", notes=session["notes"])
