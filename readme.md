# Bus Delay Analysis

This project analyzes bus stop and route data to identify patterns and potential causes of delays.

## Data Source

The analysis uses two main datasets, assumed to be provided as CSV files within a `data/` directory:
- `stop_times.csv`: Contains information about scheduled and actual arrival/departure times at bus stops.
- `trips.csv`: Contains details about bus trips, including route information.

## Setup

To run this analysis, ensure you have the `stop_times.csv` and `trips.csv` files available, ideally within a `data/` subdirectory. The notebook assumes these files are loaded either directly or extracted from a `.zip` archive.

1.  **Upload Data**: Upload an `archive.zip` file containing `stop_times.csv` and `trips.csv` if running in an environment like Google Colab.
2.  **Extract Data**: The notebook includes code to extract these files into a `data/` directory.
3.  **Install Libraries**: Ensure `pandas`, `numpy`, and `matplotlib` are installed.

## Analysis Steps

The notebook performs the following key steps:

1.  **Data Loading and Preprocessing**:
    *   Loads `stop_times.csv` and `trips.csv` into pandas DataFrames.
    *   Converts `arrival_time` and `departure_time` columns to datetime objects.
    *   Calculates `delay` in minutes for each stop (`departure_time - arrival_time`).
    *   Extracts the `hour` of arrival for time-based analysis.

2.  **Bus Activity Analysis**:
    *   Identifies peak hours for bus activity by counting the number of stops per hour.
    *   Visualizes peak bus activity using a bar chart.

3.  **Delay Analysis**:
    *   **Average Delay by Hour**: Calculates and visualizes the average delay across all stops for each hour of the day.
    *   **Top Routes with Highest Delays**: Merges trip data to link stop times with routes, then identifies and visualizes the top 10 routes with the highest average delays.
    *   **Top Stops with Highest Delays**: Identifies and visualizes the top 10 individual stops with the highest average delays.

4.  **Peak vs. Non-Peak Delay Comparison**:
    *   Categorizes hours into 'Peak' (e.g., 8-10 AM, 5-7 PM) and 'Non-Peak' periods.
    *   Compares average delays between peak and non-peak periods using a bar chart.

5.  **Delay Intensity Heatmap**:
    *   Generates a heatmap to visualize delay intensity across different hours.

6.  **Simulated Delays (Demonstration)**:
    *   Includes sections to simulate more realistic delay data using `numpy.random.normal` for demonstration purposes, showing how the visualizations would look with varying delay patterns.
