#copyright Shirley Nelson @2019
import datetime
import holidays
from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__,static_url_path='/static/',static_folder='/static/')
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
notesglobal = []
toptitle="Shirley Nelson Resume"

@app.route("/contactmoreindex")
def contactmoreindex():
    return render_template("contactmoreindex.html")

@app.route("/contactmore")
def contactmore():
    return render_template("contactmore.html")
@app.route("/contactmore1")
def contactmore1():
    return render_template("contactmore1.html")
@app.route("/contactmore2")
def contactmore2():
    return render_template("contactmore2.html")
@app.route("/contactmore3")
def contactmore3():
    return render_template("contactmore3.html")
@app.route("/contactmore4")
def contactmore4():
    return render_template("contactmore4.html")
@app.route("/contactmore5")
def contactmore5():
    return render_template("contactmore5.html")
@app.route("/contactmore6")
def contactmore6():
    return render_template("contactmore6.html")
@app.route("/contactmore7")
def contactmore7():
    return render_template("contactmore7.html")
@app.route("/contactmore8")
def contactmore8():
    return render_template("contactmore8.html")

@app.route("/blog", methods=["GET", "POST"])
def blog():
    if request.method == "POST":
        noteglobal = request.form.get("noteglobal")
        notesglobal.append(noteglobal)

    return render_template("blog.html", notesglobal=notesglobal)

@app.route("/privateblog", methods=["GET", "POST"])
def privateblog():
    if session.get("notes") is None:
        session["notes"]=[]
    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)

    return render_template("privateblog.html", notes=session["notes"])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/python")
def python():
    return render_template("python.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/hello", methods=["GET","POST"])
def hello():
    if request.method == "GET":
        return "Please submit the form instead."
    else:
        name = request.form.get("name")
        return render_template("hello.html", name=name)

@app.route("/travelsearch")
def travelsearch():
    return render_template("travelsearch.html")

@app.route("/travels", methods=["GET","POST"])
def travels():
    if request.method == "GET":
        return "Please submit the form instead."
    else:
        radio_flight=request.form.get("radio_flight")
        radio_cruise=request.form.get("radio_cruise")
        radio_car=request.form.get("radio_car")
        radio_hotel=request.form.get("radio_hotel")
        departure_location=request.form.get("departure_location")
        departure_destination_location=request.form.get("departure_destination_location")
        departure_date=request.form.get("departure_date")
        departure_partofday=request.form.get("departure_partofday")
        departure_return_date=request.form.get("departure_return_date")
        departure_return_partofday=request.form.get("departure_return_partofday")
        return render_template("travelsearch.html",radio_flight=radio_flight,radio_cruise=radio_cruise,radio_car=radio_car,radio_hotel=radio_hotel,departure_location=departure_location,departure_destination_location=departure_destination_location,departure_date=departure_date,departure_partofday=departure_partofday,departure_return_date=departure_return_date,departure_return_partofday=departure_return_partofday)
