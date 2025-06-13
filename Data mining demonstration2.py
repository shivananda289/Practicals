import pandas as pd
import matplotlib.pyplot as plt
data={
    "SaleID": [1, 2, 3, 4, 5, 6],
    "CustomerID": [101, 102, 103, 104, 105, 106],
    "Region": ["North", "South", "North", "East", "West", "South"],
    "Quantity": [2, 3, 1, 5, 2, 4],
    "Price": [500, 300, 700, 200, 150, 300],
    "TotalAmount": [1000, 900, 700, 1000, 300, 1200],
}
sales_data=pd.DataFrame(data)
region_sales=sales_data.groupby("Region") ["TotalAmount"].sum().reset_index()
print("Total Sales by Region:")
print(region_sales)
plt.figure(figsize=(8, 5))
plt.bar(region_sales["Region"], region_sales ["TotalAmount"], color=["skyblue", "orange", "green", "red"])
plt.title("Total Sales by Region", fontsize=16)
plt.xlabel("Region", fontsize=12)
plt.ylabel("Total Sales (USD)", fontsize=12)
plt.grid(axis="y")
plt.show()
