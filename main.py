import pandas
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def station_temperature(station, date):
    filename = ("data_small/TG_STAID" + str(station).zfill(6) + ".txt")
    print(filename)
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    return {"station": station, "date": date, "temperature": temperature}
    # temperature is an int.  If you don't wrap it as follows str(temperature),
    # then your web page will display TypeError: The view function did
    # not return a valid response. The return type must be a string, dict,
    # list, tuple with headers or status, Response instance, or WSGI callable,
    # but it was a int. Better is to return a dict
    # df = pd.read_csv("data/" + station + "/" + date + ".csv")
    # return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)