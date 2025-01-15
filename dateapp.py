from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    day_of_week = None
    if request.method == "POST":
        try:
            month = int(request.form["month"])
            day = int(request.form["day"])
            year = int(request.form["year"])
            date = datetime(year, month, day)
            day_of_week = date.strftime("%A")
        except ValueError:
            day_of_week = "Invalid date. Please try again."
    return render_template("index1.html", day_of_week=day_of_week)

if __name__ == "__main__":
    app.run(debug=True)