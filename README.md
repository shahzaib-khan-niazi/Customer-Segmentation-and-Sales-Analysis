# Customer-Segmentation-and-Sales-Analysis
Customer-Segmentation-and-Sales-Analysis on Python
This Python script performs exploratory data analysis (EDA) on a sales dataset (Sample - Superstore.csv). It leverages Pandas for data manipulation, Matplotlib and Seaborn for data visualization, and NumPy for numerical operations.

1)Key Features & Analysis Performed:
Data Loading & Inspection
Reads a compressed ZIP CSV file with Latin-1 encoding.
Displays the first few rows of the dataset (.head()).
Prints dataset information (.info()).
Removes duplicate entries.

2)Customer Segmentation Analysis:
Identifies different customer segments (based on the Segment column).
Counts the number of customers in each segment.
Visualizes customer distribution using a pie chart.

3)Sales Analysis per Customer Segment:
Groups sales data by customer segment and calculates total sales.
Creates bar and pie charts to illustrate sales distribution by segment.

4)Customer Order Frequency Analysis:
Counts the number of orders placed by each customer.
Identifies repeat customers and sorts them by total orders.
Displays the top 12 customers with the highest number of orders.

5)Top Spending Customers:
Calculates total sales per customer.
Sorts customers by highest sales volume.
Displays the top 12 highest spending customers.

6)Shipping Mode Analysis:
Counts the usage frequency of each shipping mode.
Visualizes shipping mode distribution using a pie chart.

Python Libraries Used:
pandas — for data processing and aggregation
matplotlib.pyplot — for data visualization (bar charts, pie charts)
seaborn — for statistical data visualization
numpy — for numerical operations
