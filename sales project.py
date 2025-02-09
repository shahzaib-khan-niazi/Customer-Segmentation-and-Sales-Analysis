import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Load the CSV data with zip compression and latin1 encoding
salespro = pd.read_csv(r"C:\Users\shahz\PycharmProjects\hello\Sample - Superstore.csv (1).zip", compression='zip', encoding='latin1')

# Print initial data and info
print(salespro.head())
print("\n", salespro.info())
print("\n", salespro.drop_duplicates())

# Types of customer
print("\n TYPES OF CUSTOMER ", salespro["Segment"].unique())

# Count the number of customers for each segment
number_of_customers = salespro["Segment"].value_counts().reset_index()
number_of_customers.columns = ['Type of Customer', 'Count']  # Rename columns for clarity

# Print the DataFrame to ensure renaming is correct
print("\n ", number_of_customers)

plt.pie(number_of_customers['Count'], labels=number_of_customers['Type of Customer'], autopct='%1.1f%%')
# Display the plot
plt.show()
sales_per_segment = salespro.groupby('Segment')['Sales'].sum().reset_index()
sales_per_segment = sales_per_segment.rename(columns={'Segment' : 'Type Of Customer', 'Sales' : 'Total Sales'})

print("\n",sales_per_segment)
plt.bar(sales_per_segment['Type Of Customer'], sales_per_segment['Total Sales'])
plt.show()
plt.pie(sales_per_segment['Total Sales'], labels=sales_per_segment['Type Of Customer'], autopct='%1.1f%%')
plt.show()
customers_order_frequency = salespro.groupby(['Customer ID', 'Customer Name', 'Segment'])['Order ID'].count().reset_index()
customers_order_frequency.rename(columns={'Order ID': 'Total Orders'}, inplace=True)
repeat_customers = customers_order_frequency[customers_order_frequency['Total Orders'] >= 1]
repeat_customers_sorted = repeat_customers.sort_values(by='Total Orders', ascending=False)
print("\n",repeat_customers_sorted.head(12).reset_index(drop=True))
customer_sales = salespro.groupby(['Customer ID', 'Customer Name', 'Segment'])['Sales'].sum().reset_index()
top_spenders = customer_sales.sort_values(by='Sales', ascending=False)
print("\n",top_spenders.head(12).reset_index(drop=True))
shipping_model = salespro['Ship Mode'].value_counts().reset_index()
shipping_model = shipping_model.rename(columns={'index':'Use Frequency', 'Ship Mode':'Mode Of Shipment', 'count' : 'Use Frequency'})
print("\n",shipping_model)
plt.pie(shipping_model['Use Frequency'], labels=shipping_model['Mode Of Shipment'], autopct='%1.1f%%')
plt.show()
state = df['State'].value_counts().reset_index()
state = state.rename(columns={'index':'State', 'State':'Number Of Customers'})
print("\n",state.head(20))
