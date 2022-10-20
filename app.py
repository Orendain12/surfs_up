import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

# 3. Define what to do when a user goes to the index route
@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')


# 4. Define what to do when a user goes to the /about route
@app.route("/api/v1.0/precipitation")

# # Create the precipition() function
# #def precipitation():
#     return

# # Add code that calculate the date one year ago from most recent date in database
# def precipitation():
#    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
#    return

# # write a query to get date and precipation for previous year.
# # add this query to existing code
# # .\ means continue query to continue to next line below 
# def precipitation():
#    precipitation = session.query(Measurement.date, Measurement.prcp).\
#       filter(Measurement.date >= prev_year).all()
#    return

# create dictionary with the date = key and precipitation = value 
# to do this you will "jsonify" dictionary....its a function that converts to dict to JSON file
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)



# Define what to do when a user goes to the /about route
@app.route("/api/v1.0/stations")

# # Create a function called stations() 
# def stations():
#     return   

# # add code to allow get all stations in database. 
# def stations():
#     results = session.query(Station.station).all()
#     return

# Unravel results into one-dimensional array. Need to use function np.ravel()
# with results as paramater
# convert our unraveled results into list . To convert results to a list. 
# Will need use the list function, which is list(), and convert that array into a list 
# Jsonfiy the list and return it as JSON file.  

def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)
    

# Define what to do when a user goes to the /about route
@app.route("/api/v1.0/tobs")


# Create function called temp_monthly() 
# def temp_monthly():
#     return

# # Add code that calculate the date one year ago from most recent date in database
# def temp_monthly():
#     prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
#     return

# # Query primary station for all temperature observations from previous year
# def temp_monthly():
#     prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
#     results = session.query(Measurement.tobs).\
#         filter(Measurement.station == 'USC00519281').\
#         filter(Measurement.date >= prev_year).all()
#     return


# # Unravel the results into a one-dimensional array and convert that array into a list 
# # Jsonify the list and return results
# def temp_monthly():
#     prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
#     results = session.query(Measurement.tobs).\
#       filter(Measurement.station == 'USC00519281').\
#       filter(Measurement.date >= prev_year).all()
#     temps = list(np.ravel(results))


# Jsonify our temps list and then return it.
# add the return statement to end of code 
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)



# Creating the Statistics Route 
# report the min, avg, and max temperatures
# this route will need to provide both a start and ending date

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")


# Create a function called stats()
# def stats():
#      return


# # Add parameters to stats() function.
# # a start parameter and aan end parameter
# def stats(start=None, end=None):
#      return


# # Function declared, create a query to select min, avg, and max temperatures from SQLite database
# # create a list called sel
# def stats(start=None, end=None):
#     sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]


# Determine start and end date by adding "if-no"t" statement 
# If-not statment helps accomplish query database into list and help unravel results
# into one-dimensional array and convert then to a list
# Jsonfiy results and return them
# def stats(start=None, end=None):
#     sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

#     if not end:
#         results = session.query(*sel).\
#             filter(Measurement.date >= start).all()
#         temps = list(np.ravel(results))
#         return jsonify(temps=temps)


# Calculate tempature min,avg, max with start and end dates. Use "sel" list 
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)



if __name__ == "__main__":
    app.run(debug=True)








