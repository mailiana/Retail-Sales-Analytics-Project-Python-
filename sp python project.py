import pandas as pd
sales = pd.read_csv(r'c:\Users\zonky\OneDrive\Desktop\EP Class\retail_sales_dataset.csv')
products = pd.read_csv(r'c:\Users\zonky\OneDrive\Desktop\EP Class\products_data.csv')
customers = pd.read_csv(r'c:\Users\zonky\OneDrive\Desktop\EP Class\customers_data.csv')

print(sales)
print(sales.head())
print(sales.info())

print(products)
print(products.head())
print(products.info())

print(customers)
print(customers.head())
print(customers.info())

desc = sales.describe(include='all')
print(desc)

customers_desc = customers.describe(include='all')
print(customers_desc)

products_desc = products.describe(include='all')
print(products_desc)

# Normalize column names
sales.columns = sales.columns.str.strip().str.lower().str.replace(' ', '_')
print(sales.columns)
# compute total sales
total_sales = sales['quantity'] * sales['price_per_unit']
print(total_sales)
sales['total_amount'] = total_sales



import datetime as dt
ref_date = dt.datetime(2024, 1, 1)
print(ref_date)
# ensure 'date' is a datetime dtype before computing recency
sales['date'] = pd.to_datetime(sales['date'], errors='coerce')
print(sales['date'].dtype)
sales['recency'] = (ref_date - sales['date']).dt.days
print(sales[['date', 'recency']].head())


import matplotlib.pyplot as plt
import seaborn as sns

print(sales['total_amount'].describe())
# Visualize sales distribution
plt.figure(figsize=(10, 6))
sns.histplot(sales ['total_amount'], bins=30, kde=True)
plt.title('Sales Distribution')
plt.xlabel('Total Amount')
plt.ylabel('Frequency')     
plt.show()

# Revenue by product category (handle missing categories, sort descending)
sales['product_category'] = sales['product_category'].fillna('Unknown')
print(sales['product_category'].unique())

revenue_by_category = sales.groupby('product_category')['total_amount'].sum().sort_values(ascending=False)

plt.figure(figsize=(10,6))
sns.barplot(x=revenue_by_category.index, y=revenue_by_category.values, palette='viridis')
plt.title("Revenue by Product Category")
plt.ylabel("Total Revenue")
plt.xlabel("Product Category")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# annotate bars with formatted amounts
for i, v in enumerate(revenue_by_category.values):
                plt.text(i, v, f'${v:,.2f}', ha='center', va='bottom', fontsize=9)

plt.show()
