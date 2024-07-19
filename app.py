# Import the dependencies.
from flask import Flask, jsonify
import datetime as dt
import numpy as np
import pandas as pd
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

#################################################
# Database Setup
#################################################

# Create engine to connect to the SQLite database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect the existing database into a new model
Base = automap_base()
Base.prepare(autoload_with=engine)

# Map the classes
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)


#################################################
# Repeated Functions
#################################################
#Create function to calculate most recent data and one year ago 
def get_most_recent_date_and_one_year_ago():
    """Calculate the most recent date and the date one year ago"""
    most_recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    most_recent_date = dt.datetime.strptime(most_recent_date, "%Y-%m-%d")
    one_year_ago = most_recent_date - dt.timedelta(days=365)
    return most_recent_date, one_year_ago
#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available API routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )
#Precipitation Route 

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return the precipitation data for the last year"""
    # Get the most recent date and the date one year ago
    most_recent_date, one_year_ago = get_most_recent_date_and_one_year_ago()

    # Perform a query to retrieve the data and precipitation scores for the last year
    precipitation_data = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= one_year_ago).all()
    
    session.close()

    # Convert the query results to a dictionary with date as the key and prcp as the value
    precipitation_list = [{"date": date, "prcp": prcp} for date, prcp in precipitation_data]

    return jsonify(precipitation_list)

#Stations Route

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a JSON list of stations from the dataset"""
    # Perform a query to retrieve the stations data
    stations_data = session.query(Station.station).distinct().all()

    session.close()

 # Convert the query results
    stations_list = list(np.ravel(stations_data))

    return jsonify(stations_list)

#TOBS Route

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a JSON list of temperature observations (TOBS) of the most active station for the previous year"""
    # Find the most active station
    most_active_station = session.query(Measurement.station, func.count(Measurement.id)).\
        group_by(Measurement.station).\
        order_by(func.count(Measurement.id).desc()).first()[0]

   # Get the most recent date and the date one year ago
    most_recent_date, one_year_ago = get_most_recent_date_and_one_year_ago()

    # Perform a query to retrieve the temperature observations for the last year
    tobs_data = session.query(Measurement.date, Measurement.tobs, Station.name).\
        filter(Measurement.station == most_active_station).\
        filter(Measurement.date >= one_year_ago).\
        join(Station, Measurement.station == Station.station).all()

    session.close()

    # Convert the query results 
    tobs_list = [{"station": station, "date": date, "tobs": tobs} for date, tobs, station in tobs_data]

    return jsonify(tobs_list)

#Dynamic Route 
#Start route + start/end route grouped together to follow DRY
@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def temperature_stats(start, end=None):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range"""
    # Convert the start and end dates to datetime. 
    #Set end date to most recent date if not specified 
    start_date = dt.datetime.strptime(start, "%Y-%m-%d")
    if end:
        end_date = dt.datetime.strptime(end, "%Y-%m-%d")
    else:
        end_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
        end_date = dt.datetime.strptime(end_date, "%Y-%m-%d")

    # Perform a query to retrieve the temperature statistics for the date range
    temperature_stats = session.query(
        func.min(Measurement.tobs),
        func.avg(Measurement.tobs),
        func.max(Measurement.tobs)
    ).filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

    session.close()

    # Convert the query results 
    temperature_stats_list = [{"TMIN": min_temp, "TAVG": avg_temp, "TMAX": max_temp} 
                              for min_temp, avg_temp, max_temp in temperature_stats]


    return jsonify(temperature_stats_list)

if __name__ == "__main__":
    app.run(debug=True, port=5001)