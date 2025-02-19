## 2️⃣ Data Cleaning Script (scripts/data_cleaning.py)

import pandas as pd

# Load Data
df = pd.read_csv("../data/sales_data.csv")

# Convert Date Column to DateTime
df["Date"] = pd.to_datetime(df["Date"])

# Check for Missing Values
df.fillna(0, inplace=True)

# Add New Columns
df["Profit Margin %"] = round((df["Profit"] / df["Revenue"]) * 100, 2)

# Save Cleaned Data
df.to_csv("../data/cleaned_sales_data.csv", index=False)
print("Data Cleaning Completed!")