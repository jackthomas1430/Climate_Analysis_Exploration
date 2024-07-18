# Module 10 SQLAlchemy Challenge: Climate Analysis and Exploration

## Overview
For the module 10 challenge, we perform climate analysis and data exploration of a climate database using Python and SQLAlchemy. The analysis is divided into two main parts: using Jupyter Notebook to do data analysis and building a Flask API to return data in JSON format.

###Part 1: Data Analysis and Exploration

The data analysis and exploration are performed in the Jupyter Notebook climate_analysis.ipynb.

Steps:

1. Database Connection:
    -Use SQLAlchemy to connect to the SQLite database hawaii.sqlite.
    -Reflect the database tables into classes.
    -Create a session to query the database.

2. Precipitation Analysis:
    -Find the most recent date in the dataset.
    -Query the last 12 months of precipitation data.
    -Save the query results into a Pandas DataFrame and plot the data using Matplotlib.
    -Calculate summary statistics data.

3. Station Analysis:
    -Calculate the total number of stations.
    -Identify the most active station 
    -Query tobs data of the most active station for the last 12 months.
    -Calculate the minimum, maximum, and avg temperatures for the most active station.
    -Plot the tobs as a histogram.

###Part 2: Building the Flask API
####Available Routes:
    1.Homepage (/):
        -Lists all available routes.
    2. Precipitation Data (/api/v1.0/precipitation):
        -Returns the last 12 months of precipitation data.
    3. Stations Data (/api/v1.0/stations):
        -Returns a list of all stations.
    4. Temperature Observations (/api/v1.0/tobs):
        -Returns the last 12 months of temperature observations for the most active station. 
    5. Temperature Statistics (/api/v1.0/<start> and /api/v1.0/<start>/<end>):
        -Returns the minimum, average, and maximum temperatures for a specified start or start-end range.

## Files
- 'sqlalchemy-challenge'(https://github.com/jackthomas1430/sqlalchemy-challenge.git) :The main repo for this challenge. 
- 'SurfsUp': Directory containing the main flask application script 'app.py' and Jupyter Notebook 'climate_analysis.ipyn'
    - 'app.py': Main Flask application script.
    - 'climate_starter.ipyn'`: Jupyter Notebook containing data analysis and exploration.
- 'Resources': Directory containing data files ('hawaii_measurements.csv','hawaii_stations.csv') 'hawaii.sqlite').
- 'Results': Directory containing images of the results 

## Instructions
1. Ensure the following have been installed:
- Python 
- Jupyter Notebook
- Flask
- SQLAlchemy
- Pandas
- Matplotlib
2. Clone the repository to your local device using git clone <https://github.com/jackthomas1430/sqlalchemy-challenge.git>
3. Open 'climate_analysis.ipyn' and run to find data analysis results
4. Open 'app.py' to run Flask application script
    -to run the flask app use the following command python app.py
    
##Results 
-Images of the results can be found in the 'Results' folder located in sqlalchemy-challenge repo. 

##Acknowledgements
    Xpert Learning Assistant was used to answer detailed questions, and assist in debugging.For more information about the Xpert Learning Assistant, visit [EdX Xpert Learning Assistant](https://www.edx.org/). 
    
##References
1. Python Datetime Documentation- [Python Datetime Documentation](https://docs.python.org/3/library/datetime.html#datetime.date.strftime)
2. Dunder (Magic) Methods in Python- [Dunder (Magic) Methods in Python](https://www.geeksforgeeks.org/dunder-magic-methods-python/)
3. HTML Tags Reference- [HTML Tags Reference](https://www.w3schools.com/TAGs/)
4. Python OOP Concepts- [Python OOP Concepts](https://www.geeksforgeeks.org/python-oops-concepts/)
5. Difference Between filter and filter_by in SQLAlchemy- [Difference Between filter and filter_by in SQLAlchemy](https://stackoverflow.com/questions/2128505/difference-between-filter-and-filter-by-in-sqlalchemy)
6. SQLAlchemy SQLite Dialect Documentation- [SQLAlchemy SQLite Dialect Documentation](https://docs.sqlalchemy.org/en/20/dialects/sqlite.html)
7. Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910, https://journals.ametsoc.org/view/journals/atot/29/7/jtech-d-11-00103_1.xmlLinks to an external site.
