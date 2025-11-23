# Retail-Sales-Analytics-Project-Python-
**Data With Miss Mailiana** — *November Class*  Comprehensive data analytics project using Python, Pandas, Matplotlib, Seaborn.

#  **Project Overview**

This repository contains a full Python project analyzing **Retail Sales Data**, including:

* Data loading & understanding
* Data cleaning & preparation
* Exploratory data analysis (EDA)
* Basic statistics & insights
* Visualizations (distribution, category analysis)
* Computed KPIs
* Date formatting & column normalization

This project was completed as part of the **November Data Analytics Weekend Class** under *Data With Miss Mailiana*.


#  **1. Objective**

The goal of this project is to:

* Understand customer behavior
* Analyze product performance
* Study revenue patterns
* Generate business insights
* Build foundational Python analytics skills

The project implements the **Data Analytics Lifecycle**:

1. Define objective
2. Load & understand data
3. Data cleaning
4. Exploratory data analysis
5. Visualization & insights


#  **2. Dataset Description**

Three datasets were used:

###  **Sales Dataset**

Contains all transactions:

* Order ID
* Date
* Customer ID
* Gender
* Age
* Product category
* Quantity
* Unit price
* Total amount

###  **Customer Dataset**

* Customer demographics
* Age
* Country
* Gender

###  **Product Dataset**

* Product name
* Category
* Supplier
* Price & cost


# **3. Technologies Used**

| Tool       | Purpose                      |
| ---------- | ---------------------------- |
| Pandas     | Loading & cleaning data      |
| NumPy      | Numeric operations           |
| Matplotlib | Visualizations               |
| Seaborn    | Styled statistical charts    |
| Python     | Primary programming language |


#  **4. Project Steps**

## **✔ Step 1 — Import Libraries**

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

## **✔ Step 2 — Load Datasets**

```python
sales = pd.read_csv("sales_data.csv")
products = pd.read_csv("products_data.csv")
customers = pd.read_csv("customers_data.csv")
```


## **✔ Step 3 — Preview & Inspect Data**

```python
sales.head()
sales.info()
products.info()
customers.info()
```

Purpose: understand structure, datatypes, missing values.


## **✔ Step 4 — Data Cleaning**

### Normalize column names:

```python
sales.columns = sales.columns.str.replace(" ", "_")
```

### Convert dates:

```python
sales['date'] = pd.to_datetime(sales['date'])
```

### Compute total sales:

```python
sales['total_sales'] = sales['quantity'] * sales['unitprice']
```


## **✔ Step 5 — Exploratory Data Analysis**

```python
sales.describe()
customers.describe()
products.describe()
```

### Insights generated include:

* Frequency of product categories
* Mean age of customers
* Average quantity purchased
* Min–max product price
* Average selling amount
* Total customers
* Unique countries (5)
* Most bought price range
* Age distribution

These insights help understand purchase behavior & revenue patterns.


# 📈 **6. Visualizations**

## **✔ Sales Distribution Chart**

```python
sns.histplot(sales['total_amount'], bins=30)
plt.title("Distribution of Total Sales")
plt.show()
```

## **✔ Product Category Chart**

```python
sns.countplot(data=sales, x='product_category')
plt.xticks(rotation=45)
plt.title("Product Category Frequency")
plt.show()
```

*Figure 1*
<img width="1000" height="600" alt="Figure_1" src="https://github.com/user-attachments/assets/5975f365-7557-4372-a739-3159f5b86d27" />

*Figure 2*
<img width="1000" height="600" alt="Figure_2" src="https://github.com/user-attachments/assets/28a70c37-e268-41b6-8f45-2e371bbf9834" />


#  **7. Key Insights**

### ⭐ Sales Insights

* Most purchase amounts fall between **GHS 0–250**
* Electronics & Fashion show strong purchase volumes

### ⭐ Customer Insights

* Customers aged **30–45** purchase the most
* 5 unique countries represented

### ⭐ Product Insights

* Certain categories dominate the revenue
* Quantity purchased averages between **2–3 items**


# **8. Conclusion**

This project demonstrates foundational Python analysis including:

* Data preparation
* Basic EDA
* Visualization
* Generating actionable insights

Students can confidently use this project in their **portfolio, GitHub, and job applications**.
