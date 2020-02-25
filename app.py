#create list of stations
stations = [
    'USC00519281', 
    'USC00519397', 
    'USC00513117', 
    'USC00519523',
    'USC00516128',
    'USC00514830',
    'USC00511918',
    'USC00517948',
    'USC00518838']


#import Flask
from flask import Flask, jsonify

#create an app
app = Flask(__name__)

#define the app
@app.route("/")
def home():
    return (
        f"Hello!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def prcp():
    return (
        prcp_dict
    

@app.route("/api/v1.0/stations")
def stations():
    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():
    return tobs

@app.route("/api/v1.0/<start>")
def start():
    return

@app.route("/api/v1.0/<start>/<end>")
def start():
    return


    