## 1️⃣ Add a Sample Dataset (data/sales_data.csv)

import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()
categories = ["Fruits", "Bakery", "Dairy", "Beverages"]
products = {"Fruits": ["Apples", "Bananas", "Oranges"], "Bakery": ["Bread", "Cake"], "Dairy": ["Milk", "Cheese"], "Beverages": ["Juice", "Tea"]}

data = []
for _ in range(500):
    category = np.random.choice(categories)
    product = np.random.choice(products[category])
    data.append([
        fake.date_this_year(),
        np.random.choice(["London", "Leeds", "Birmingham"]),
        product,
        category,
        np.random.randint(50, 500),
        np.random.randint(100, 1000),
        np.random.randint(20, 300),
        round(np.random.uniform(3.0, 5.0), 1)
    ])

df = pd.DataFrame(data, columns=["Date", "Store", "Product", "Category", "Units Sold", "Revenue", "Profit", "Customer Feedback"])
df.to_csv("sales_data.csv", index=False)
print("Sample dataset created!")