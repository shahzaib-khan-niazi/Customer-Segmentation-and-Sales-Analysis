import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

file_path = r"C:\Users\shahz\PycharmProjects\hello\Sample - Superstore.csv (1).zip"
salesproj = pd.read_csv(file_path, compression='zip', encoding='latin1')
print(salesproj.info(),'\t',salesproj.describe())
print('\nchecking null values\n',salesproj.isnull().sum())
print('\nchecking duplicates\n',salesproj.duplicated())

cus_and_seg=(salesproj.groupby(['Customer Name'])['Segment'].first())
cus_and_seg.columns=['Customer Name','Occupation']
print('\n checking customer and their occupation\n',cus_and_seg)

print('\n total customers\n',salesproj['Customer Name'].count().sum())

orders = salesproj.groupby('Customer Name')['Order ID'].nunique().reset_index()
orders.columns = ['Customer Name', 'Customer Orders']
top_orders = orders.sort_values(by='Customer Orders', ascending=False).head(10)
print('\nCustomers with top 10 most orders:\n', top_orders)

product_sales=salesproj.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(12,7))
x_axis=product_sales.index
y_axis=product_sales.values
plt.bar(x_axis,y_axis,color='g')
plt.xlabel('Name of products')
plt.ylabel('Product sales')
plt.title('Top 10 Products by Sales')
plt.xticks(rotation=75)
plt.grid(True)
plt.show()

sales_state=salesproj.groupby('State')['Sales'].sum().sort_values(ascending=False)
plt.figure(figsize=(12,7))
x_axis=sales_state.index
y_axis=sales_state.values
sns.scatterplot(x=x_axis,y=y_axis,color='r',s=100)
plt.title('Top 10 States by Sales')
plt.xlabel('State')
plt.ylabel('Total Sales')
plt.xticks(rotation=90)
plt.grid(True)
plt.tight_layout()
plt.show()

shipment_unique_orders = salesproj.groupby('Ship Mode')['Order ID'].nunique().sort_values(ascending=False)
print("\nUnique Orders per Ship Mode:\n", shipment_unique_orders, "\n")
shipment_line_items = salesproj['Ship Mode'].value_counts()
print("\ntotal Line Items per Ship Mode:\n", shipment_line_items)

salesproj['Ship Date'] = pd.to_datetime(salesproj['Ship Date'])
salesproj['Order Date'] = pd.to_datetime(salesproj['Order Date'])
salesproj['Shipping Time (Days)'] = (salesproj['Ship Date'] - salesproj['Order Date']).dt.days
avg_shipping = salesproj.groupby('Ship Mode')['Shipping Time (Days)'].mean().sort_values()
print('\naverage delivery duration per order\n',avg_shipping)

alls=[
salesproj['Profit'].sum(),
salesproj['Discount'].sum(),
salesproj['Quantity'].sum()
]
label=['Profit','Discount','Quantity']
color=['grey','orange','white']
plt.pie(alls,labels=label, autopct='%1.1f%%', colors=color, startangle=140)
plt.title('Proportion of Quantity, Discount, and Profit')
plt.show()

profit_by_subcat = salesproj.groupby(['Category', 'Sub-Category'])['Profit'].sum().reset_index()
profit_by_subcat.columns = ['Category', 'Sub-Category', 'Total Profit']
profit_by_subcat = profit_by_subcat.sort_values(by='Total Profit')
print("\n total Profit by Category and Sub-Category:\n")
print(profit_by_subcat.to_string(index=False))

top_states = salesproj.groupby('State')['Sales'].sum().sort_values(ascending=False).head(10).index
top_states = salesproj[salesproj['State'].isin(top_states)]
plt.figure(figsize=(12, 7))
sns.boxplot(x='State', y='Sales', data=top_states)
plt.title('Distribution of Sales in Top 10 States')
plt.xlabel('State')
plt.ylabel('Sales Amount')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()


sales=salesproj['Sales'].values
profit=salesproj['Profit'].values
discount=salesproj['Discount'].values
print("\nmean:\n", np.mean(sales))
print("\nmedian:\n", np.median(sales))
print("\nmax Sale:\n", np.max(sales))
print("\nmin Sale:\n", np.min(sales))
total_profit=np.sum(salesproj['Profit'])
total_orders = salesproj['Order ID'].nunique()
avg_profit_persale=total_profit/total_orders
print(f"\nAverage Profit per Sale: \n{avg_profit_persale:.2f}")

efficiency = np.where(sales != 0, profit / sales, 0)
print("\nmean efficiency:\n", np.mean(efficiency))
print("\nmax efficiency:\n", np.max(efficiency))
print("\nmin efficiency:\n", np.min(efficiency))

plt.figure(figsize=(8,6))
plt.hist(efficiency, bins=50, color='blue', edgecolor='pink')
plt.title('distribution of profit efficiency ')
plt.xlabel('profit per $1 Sale')
plt.ylabel('number of orders')
plt.grid(True)
plt.tight_layout()
plt.show()

from sklearn.linear_model import LinearRegression
y=salesproj[['Profit']].values
X=salesproj[['Sales']].values
model=LinearRegression()
model.fit(X,y)
salesproj['Predicted profit']=model.predict(X)
print(salesproj[['Sales', 'Profit', 'Predicted profit']].head(11))


y=salesproj['Discount'].values
X=salesproj[['Quantity']].values
model=LinearRegression()
model.fit(X,y)
pred_y=model.predict(X)
plt.figure(figsize=(10,7))
sns.scatterplot(x=salesproj['Quantity'], y=salesproj['Discount'], label='Actual')
plt.plot(salesproj['Quantity'], pred_y, color='red', label='Regression Line')
plt.title('Linear Regression: Predicting Discount based on Quantity')
plt.xlabel('Quantity')
plt.ylabel('Discount')
plt.legend()
plt.grid(True)
plt.show()
