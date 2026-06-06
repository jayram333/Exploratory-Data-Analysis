import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

print("\nDataset:")
print(df)

print("\nSummary Statistics:")
print(df.describe())

print("\nTotal Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())

df.groupby("Product")["Sales"].sum().plot(kind="bar")
plt.title("Sales by Product")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()
