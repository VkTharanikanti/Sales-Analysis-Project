## 4️⃣ Data Visualization (scripts/visualization.py)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
df = pd.read_csv("../data/cleaned_sales_data.csv")

# Revenue Trend Over Time
plt.figure(figsize=(10, 5))
df.groupby("Date")["Revenue"].sum().plot()
plt.title("Revenue Over Time")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.savefig("../data/revenue_trend.png")
plt.show()

# Best Selling Products
plt.figure(figsize=(10, 5))
top_products = df.groupby("Product")["Units Sold"].sum().nlargest(5)
sns.barplot(x=top_products.index, y=top_products.values)
plt.title("Top 5 Best-Selling Products")
plt.savefig("../data/top_products.png")
plt.show()