#import Flask
from flask import Flask, jsonify

#create an app
app = Flask(__name__)

#define the app
@app.route("/")
def home():
    return "Hello"

@app.route("/api/v1.0/precipitation")
def prcp():
    return prcp_dict

@app.route("/api/v1.0/stations")
def stations():
    return stations

@app.route("/api/v1.0/tobs")
def tobs():
    return tobs

@app.route("/api/v1.0/<start>")


@app.route("/api/v1.0/<start>/<end>")



    