import datetime
import holidays
from flask import Flask, render_template, request

app = Flask(__name__,static_url_path='/static/',static_folder='/static/')
toptitle="Shirley Nelson Resume"
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
        return render_template("travels.html",radio_flight=radio_flight,radio_cruise=radio_cruise,radio_car=radio_car,radio_hotel=radio_hotel,departure_location=departure_location,departure_destination_location=departure_destination_location,departure_date=departure_date,departure_partofday=departure_partofday,departure_return_date=departure_return_date,departure_return_partofday=departure_return_partofday)
