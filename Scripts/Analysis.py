## 3️⃣ Exploratory Data Analysis (EDA) (scripts/analysis.py)

import pandas as pd

# Load Cleaned Data
df = pd.read_csv("../data/cleaned_sales_data.csv")

# Basic Insights
print(df.describe())

# Top 5 Best-Selling Products
best_sellers = df.groupby("Product")["Units Sold"].sum().sort_values(ascending=False)
print("Best Selling Products:\n", best_sellers.head())

# Sales Trend Over Time
df["Date"] = pd.to_datetime(df["Date"])
daily_sales = df.groupby("Date")["Revenue"].sum()

# Save Insights
best_sellers.to_csv("../data/best_sellers.csv")
daily_sales.to_csv("../data/daily_sales.csv")
print("EDA Completed!")