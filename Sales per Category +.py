# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 15:09:38 2025

@author: miroz
"""



import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



# Load data
customers = pd.read_csv("customers.csv")
products = pd.read_csv("products.csv")
sales = pd.read_csv("sales.csv")

print(customers.columns)

# Merge all three datasets
sales_full = sales.merge(products, on="product_id").merge(customers, on="customer_id")

# Rename customer name column for clarity
sales_full = sales_full.rename(columns={"name_y": "customer_name", "name_x": "product_name"})


print(sales_full.columns)


# -------------------------------
# 1. Total sales by product category
# -------------------------------
category_sales = sales_full.groupby("category")["quantity"].sum().sort_values(ascending=False)
print("\n🔹 Total units sold by category:\n", category_sales)

sns.barplot(x=category_sales.index, y=category_sales.values)
plt.xticks(rotation=45)
plt.title("Total Units Sold per Category")
plt.ylabel("Units Sold")
plt.xlabel("Product Category")
plt.tight_layout()
plt.show()

# -------------------------------
# 2. Revenue by category
# -------------------------------
sales_full["revenue"] = sales_full["quantity"] * sales_full["price"]
revenue_by_category = sales_full.groupby("category")["revenue"].sum().sort_values(ascending=False)
print("\n🔹 Total revenue by category:\n", revenue_by_category)

sns.barplot(x=revenue_by_category.index, y=revenue_by_category.values)
plt.xticks(rotation=45)
plt.title("Total Revenue per Category")
plt.ylabel("Revenue (€)")
plt.xlabel("Product Category")
plt.tight_layout()
plt.show()

# -------------------------------
# 3. Top 5 customers by total spend
# -------------------------------
top_customers = sales_full.groupby("customer_name")["revenue"].sum().sort_values(ascending=False).head(5)

print("\n🔹 Top 5 customers by revenue:\n", top_customers)

sns.barplot(x=top_customers.values, y=top_customers.index)
plt.title("Top 5 Customers by Revenue")
plt.xlabel("Revenue (€)")
plt.ylabel("Customer")
plt.tight_layout()
plt.show()

# -------------------------------
# 4. Sales by country
# -------------------------------
country_sales = sales_full.groupby("country")["revenue"].sum().sort_values(ascending=False)
print("\n🔹 Revenue by country:\n", country_sales)

sns.barplot(x=country_sales.index, y=country_sales.values)
plt.xticks(rotation=90)
plt.title("Revenue by Country")
plt.ylabel("Revenue (€)")
plt.xlabel("Country")
plt.tight_layout()
plt.show()

# -------------------------------
# 5. Age group analysis
# -------------------------------
# Define age groups
bins = [18, 30, 45, 60, 80]
labels = ["18–29", "30–44", "45–59", "60+"]
sales_full["age_group"] = pd.cut(sales_full["age"], bins=bins, labels=labels, right=False)

age_revenue = sales_full.groupby("age_group")["revenue"].sum()
print("\n🔹 Revenue by age group:\n", age_revenue)

sns.barplot(x=age_revenue.index, y=age_revenue.values)
plt.title("Revenue by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Revenue (€)")
plt.tight_layout()
plt.show()
