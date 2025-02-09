# Customer-Segmentation-and-Sales-Analysis
Customer-Segmentation-and-Sales-Analysis on Python
This Python script performs exploratory data analysis (EDA) on a sales dataset (Sample - Superstore.csv). It uses Pandas for data manipulation, Matplotlib & Seaborn for data visualization, and NumPy for numerical operations.

Key Features & Analysis Performed: ✅ 1. Data Loading & Inspection:

Reads a compressed ZIP CSV file with latin1 encoding. Displays the first few rows of the dataset (.head()). Prints dataset information (.info()). Removes duplicate entries. ✅ 2. Customer Segmentation Analysis:

Identifies different customer segments (Segment column). Counts the number of customers in each segment. Visualizes customer distribution using a pie chart. ✅ 3. Sales Analysis per Customer Segment:

Groups sales data by Segment and calculates total sales. Creates a bar chart and pie chart to show sales distribution. ✅ 4. Customer Order Frequency Analysis:

Counts how many orders each customer has placed. Identifies repeat customers and sorts them by total orders. Displays the top 12 repeat customers. ✅ 5. Top Spending Customers:

Groups total sales per customer. Sorts customers by highest sales volume. Displays the top 12 highest spenders. ✅ 6. Shipping Mode Analysis:

Counts the number of times each shipping mode is used. Visualizes the distribution of shipping modes using a pie chart.

Python Libraries Used: 📌 pandas → Data processing & aggregation 📌 matplotlib.pyplot → Data visualization (bar charts, pie charts) 📌 seaborn → Statistical data visualization 📌 numpy → Numerical operations
