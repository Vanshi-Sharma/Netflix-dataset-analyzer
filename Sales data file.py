import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("Sales data.csv", sep="\t")
#print(df.head(5))
df["Revenue"]=df["Units_Sold"]*df["Price"]
#print(df.head())

max_revenue_row = df[df["Revenue"] == df["Revenue"].max()]
print("Product with highest revenue:", max_revenue_row["Product"].values[0])
print("Month with highest revenue:", max_revenue_row["Month"].values[0])
print("Highest Revenue:", max_revenue_row["Revenue"].values[0])

min_revenue_row = df[df["Revenue"] == df["Revenue"].min()]
print("Product with lowest revenue:", min_revenue_row["Product"].values[0])
print("Month with lowest revenue:", min_revenue_row["Month"].values[0])
print("Lowest Revenue:", min_revenue_row["Revenue"].values[0])




monthly_revenue = df.groupby("Month")["Revenue"].sum().reset_index()
print("\nRevenue by Month:")
print(monthly_revenue)

monthly_revenue["Month"] = pd.Categorical(
    monthly_revenue["Month"],
    categories=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
    ordered=True
)

monthly_revenue = monthly_revenue.sort_values("Month")


product_unitsSold = df.groupby("Product")["Units_Sold"].sum()
print("\nUnits_Sold by Month:")
print(product_unitsSold)

product_revenue = df.groupby("Product")["Revenue"].sum().reset_index()
print("\nRevenue by Product:")
print(product_revenue)

sns.set_style("darkgrid")
fig, axs=plt.subplots(1,3,figsize=(15,5))
#line plot

sns.lineplot(data=monthly_revenue, x="Month", y="Revenue", marker="o",ax=axs[0])
sns.despine()
axs[0].set_title("Monthly Revenue Trend")

#bar plot

sns.barplot(data=product_revenue, x="Product", y="Revenue",palette="Set2",ax=axs[1])
sns.despine()
axs[1].set_title("Revenue by Product")

#pie chart
colors = ["pink", "skyblue", "lightgreen", "orange"]   
axs[2].pie(product_unitsSold.values, labels=product_unitsSold.index, autopct="%1.2f%%",shadow=True,colors=colors)
axs[2].axis("equal")
axs[2].set_title("Units Sold by Product")

plt.suptitle("Sales Dashboard", fontsize=16, fontweight="bold")
plt.tight_layout()
plt.savefig("multiplots.png")
plt.show()






