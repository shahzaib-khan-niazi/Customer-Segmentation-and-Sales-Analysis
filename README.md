# Superstore EDA & Regression 
Customer-Segmentation-and-Sales-Analysis on Python
This Python script performs exploratory data analysis (EDA) on a sales dataset (Sample - Superstore.csv). It leverages Pandas for data manipulation, Matplotlib and Seaborn for data visualization, and NumPy for numerical operations.

1️⃣ Data Loading & Initial Check
Load Superstore sales data from a ZIP CSV file.
Check basic info: data types, summary statistics.
Check for missing values and duplicate rows.

2️⃣ Customer & Segment Analysis
Group by customer name and get their segment (like consumer, corporate, home office).
Count total unique customers.
Find top 10 customers with the most orders.

3️⃣ Product Sales Analysis
Find top 10 best-selling products by total sales.
Visualize them with a bar chart.

4️⃣ State-wise Sales Analysis
Sum up sales by state.
Visualize top states with a scatter plot (sales vs state).

5️⃣ Shipping Mode Analysis
Count unique orders by shipping mode (e.g., Same Day, First Class).
Count total line items by shipping mode.
Calculate average shipping duration per mode (difference between order date & ship date).

6️⃣ Profit, Discount, Quantity Breakdown
Sum total profit, discount, and quantity sold.
Visualize their proportions in a pie chart.

7️⃣ Profit by Category & Sub-Category
Group profit by Category and Sub-Category.
Sort and display so you see which categories are most/least profitable.

8️⃣ Detailed Sales Distribution for Top States
Pick top 10 states by sales.
Plot a boxplot to show sales distribution in each top state.

9️⃣ Key Summary Stats
Calculate mean, median, max, min for sales.
Calculate total profit, total orders, and average profit per sale.
Calculate “efficiency” = profit per $1 sale.
Visualize profit efficiency with a histogram.

🔟 Predictive Modeling (Linear Regression)
Model 1: Predict profit based on sales (using scikit-learn Linear Regression).
Model 2: Predict discount based on quantity.
Visualize the second regression: scatter plot + regression line.
