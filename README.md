# Climate Analysis and Exploration

## **Project Objective**
This project aims to analyze historical climate data to uncover patterns and trends that can aid in weather prediction and regional planning. Additionally, it showcases the integration of data analysis with Flask APIs to make insights accessible via web endpoints.

---

## **Overview**
The project is divided into two main parts:

### **1. Data Analysis and Exploration**
Using Python and SQLAlchemy, climate data from an SQLite database is analyzed to:
- Understand precipitation trends.
- Evaluate temperature observations from active weather stations.
- Generate statistical insights about climate patterns.

### **2. Flask API Development**
A Flask application is built to serve analyzed climate data through accessible JSON endpoints, allowing users to retrieve information about precipitation, temperature, and statistical summaries.

---

## **Technologies Used**
- Python (Pandas, SQLAlchemy, Flask, Matplotlib)
- SQLite
- Jupyter Notebook

---

## **Repository Contents**
- `app.py`: Main Flask application script containing API route definitions.
- `climate_analysis.ipynb`: Jupyter Notebook with data analysis and visualization.
- `Resources/`: Folder containing:
  - `hawaii_measurements.csv`: Climate measurement data.
  - `hawaii_stations.csv`: Station information.
  - `hawaii.sqlite`: SQLite database used for analysis.
- `Results/`: Folder with generated plots and visualizations.

---

## **Instructions**
1. **Prerequisites:**
   - Install Python and the following libraries:
     - Flask
     - SQLAlchemy
     - Pandas
     - Matplotlib

2. **Clone the Repository:**
   ```bash
   git clone https://github.com/jackthomas1430/Climate_Analysis_Exploration.git
   ```

3. **Run the Jupyter Notebook:**
   - Open `climate_analysis.ipynb` to explore data analysis and visualizations.

4. **Run the Flask Application:**
   ```bash
   python app.py
   ```
   - Access the available routes through the local server.

---

## **API Routes**
1. `/`: Homepage listing all available routes.
2. `/api/v1.0/precipitation`: Returns the last 12 months of precipitation data.
3. `/api/v1.0/stations`: Lists all weather stations.
4. `/api/v1.0/tobs`: Provides temperature observations for the most active station over the last 12 months.
5. `/api/v1.0/<start>`: Returns min, max, and avg temperatures from the start date.
6. `/api/v1.0/<start>/<end>`: Returns min, max, and avg temperatures for a specified date range.

---

## **Results**
### **Key Insights:**
- **Precipitation Trends:**
  - Identified seasonal variations in precipitation over the year.
  - Plotted precipitation data to visualize trends.
- **Station Analysis:**
  - Highlighted the most active station based on data availability.
  - Provided statistical summaries (min, max, and avg temperatures) for this station.
- **Temperature Trends:**
  - Visualized temperature observations for the most active station.

### **Visualizations:**
- Precipitation trends over the last year.
- Histogram of temperature observations.

---

## **Business Relevance**
This project demonstrates how data analysis and APIs can:
- Enable informed decision-making in weather-sensitive industries.
- Provide historical insights for agricultural planning and tourism management.
- Serve as a foundation for predictive modeling and regional climate studies.

---

## **Acknowledgments and References**
- Global Historical Climatology Network: [Link](https://journals.ametsoc.org/view/journals/atot/29/7/jtech-d-11-00103_1.xml)
- Python and SQLAlchemy Documentation: [SQLAlchemy](https://docs.sqlalchemy.org/en/20/)
