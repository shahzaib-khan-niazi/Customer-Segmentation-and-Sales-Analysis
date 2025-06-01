import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

file_path = r"C:\Users\shahz\PycharmProjects\hello\Sample - Superstore.csv (1).zip"
df = pd.read_csv(file_path, compression='zip', encoding='latin1')
root = tk.Tk()
root.title("Superstore Sales Dashboard")
root.geometry("1000x700")
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)
style = ttk.Style()
style.theme_use('clam')

# TAB 1: CUSTOMER SEGMENT ANALYSIS 
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text='Customer Segment Analysis')
segment_counts = df['Segment'].value_counts().reset_index()
segment_counts.columns = ['Segment', 'Count']
fig1, ax1 = plt.subplots(figsize=(5, 4))
ax1.pie(segment_counts['Count'], labels=segment_counts['Segment'], autopct='%1.1f%%')
ax1.set_title("Customer Segment Distribution")
canvas1 = FigureCanvasTkAgg(fig1, master=tab1)
canvas1.draw()
canvas1.get_tk_widget().pack(pady=10)
#  TAB 2: SALES BY SEGMENT 
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text='Sales by Segment')
sales_segment = df.groupby('Segment')['Sales'].sum().reset_index()
fig2, ax2 = plt.subplots(figsize=(5, 4))
sns.barplot(data=sales_segment, x='Segment', y='Sales', hue='Segment', ax=ax2, palette='Set2', legend=False)
ax2.set_title("Total Sales by Customer Segment")
canvas2 = FigureCanvasTkAgg(fig2, master=tab2)
canvas2.draw()
canvas2.get_tk_widget().pack(pady=10)
# TAB 3: TOP CUSTOMERS 
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text='Top Customers')
customer_sales = df.groupby('Customer Name')['Sales'].sum().reset_index()
top_customers = customer_sales.sort_values(by='Sales', ascending=False).head(5)
fig3, ax3 = plt.subplots(figsize=(5, 4))
sns.barplot(data=top_customers, x='Sales', y='Customer Name', hue='Sales', ax=ax3, palette='coolwarm', legend=False)
ax3.set_title("Top 5 Customers by Sales")
canvas3 = FigureCanvasTkAgg(fig3, master=tab3)
canvas3.draw()
canvas3.get_tk_widget().pack(pady=10)
#  TAB 4: SHIP MODE
tab4 = ttk.Frame(notebook)
notebook.add(tab4, text='Ship Mode Distribution')
ship_mode = df['Ship Mode'].value_counts().reset_index()
ship_mode.columns = ['Ship Mode', 'Count']
fig4, ax4 = plt.subplots(figsize=(5, 4))
ax4.pie(ship_mode['Count'], labels=ship_mode['Ship Mode'], autopct='%1.1f%%')
ax4.set_title("Ship Mode Usage Distribution")
canvas4 = FigureCanvasTkAgg(fig4, master=tab4)
canvas4.draw()
canvas4.get_tk_widget().pack(pady=10)

# TAB 5: SALES BY CATEGORY 
tab5 = ttk.Frame(notebook)
notebook.add(tab5, text='Sales by Category')
category_sales = df.groupby('Category')['Sales'].sum().reset_index()
fig5, ax5 = plt.subplots(figsize=(5, 4))
sns.barplot(data=category_sales, x='Category', y='Sales', hue='Category', ax=ax5, palette='pastel', legend=False)
ax5.set_title("Sales by Product Category")
canvas5 = FigureCanvasTkAgg(fig5, master=tab5)
canvas5.draw()
canvas5.get_tk_widget().pack(pady=10)
root.mainloop()
