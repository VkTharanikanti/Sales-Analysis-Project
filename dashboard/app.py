
## 5️⃣ Interactive Dashboard (dashboard/app.py)

import pandas as pd
import streamlit as st

# Load Data
df = pd.read_csv("../data/cleaned_sales_data.csv")

st.title("📊 Retail Sales Dashboard")

# Total Revenue & Profit
st.metric("Total Revenue (£)", f"{df['Revenue'].sum():,.2f}")
st.metric("Total Profit (£)", f"{df['Profit'].sum():,.2f}")

# Best-Selling Products
st.subheader("🏆 Best-Selling Products")
top_products = df.groupby("Product")["Units Sold"].sum().nlargest(5)
st.bar_chart(top_products)

# Store-wise Revenue
st.subheader("📍 Revenue by Store")
store_revenue = df.groupby("Store")["Revenue"].sum()
st.bar_chart(store_revenue)

# Run: `streamlit run dashboard/app.py`