import pandas as pd
import matplotlib.pyplot as pl
import seaborn as sns
import zipfile
import os

# =========================================
# CREATE OUTPUT FOLDERS
# =========================================

os.makedirs("IMAGES", exist_ok=True)

# =========================================
# LOAD DATA FROM ZIP FILE
# =========================================

zip_path = r"DATA\Sample - Superstore.csv - Copy.zip"

with zipfile.ZipFile(zip_path, "r") as z:

    print("Files inside ZIP:")
    print(z.namelist())

    csv_file = z.namelist()[0]

    with z.open(csv_file) as f:
        df = pd.read_csv(f, encoding="latin1")

print("\nDataset Loaded Successfully")
print(df.head())

# =========================================
# DATE PROCESSING
# =========================================

df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    errors="coerce"
)

df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month

# =========================================
# TOTAL SALES
# =========================================

total_sales = df["Sales"].sum()

print("\nTotal Sales:", round(total_sales, 2))

# =========================================
# CATEGORY SALES
# =========================================

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nCategory Sales")
print(category_sales)

category_sales.plot(kind="bar", figsize=(8, 5))

pl.title("Sales by Category")
pl.xlabel("Category")
pl.ylabel("Sales")

pl.tight_layout()
pl.savefig("IMAGES/category_sales.png")
pl.show()

# =========================================
# SUB CATEGORY SALES
# =========================================

subcategory_sales = (
    df.groupby("Sub-Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSub Category Sales")
print(subcategory_sales)

subcategory_sales.plot(kind="bar", figsize=(12, 6))

pl.title("Sales by Sub Category")
pl.xlabel("Sub Category")
pl.ylabel("Sales")

pl.tight_layout()
pl.savefig("IMAGES/subcategory_sales.png")
pl.show()

# =========================================
# REGION SALES
# =========================================

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRegion Sales")
print(region_sales)

region_sales.plot(kind="bar", figsize=(8, 5))

pl.title("Sales by Region")
pl.xlabel("Region")
pl.ylabel("Sales")

pl.tight_layout()
pl.savefig("IMAGES/region_sales.png")
pl.show()

# =========================================
# TOP STATES
# =========================================

state_sales = (
    df.groupby("State")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop 10 States")
print(state_sales.head(10))

state_sales.head(10).plot(
    kind="bar",
    figsize=(12, 5)
)

pl.title("Top 10 States by Sales")
pl.xlabel("State")
pl.ylabel("Sales")

pl.tight_layout()
pl.savefig("IMAGES/top_states.png")
pl.show()

# =========================================
# MONTHLY SALES TREND
# =========================================

monthly_sales = (
    df.groupby("Month")["Sales"]
    .sum()
)

print("\nMonthly Sales")
print(monthly_sales)

monthly_sales.plot(
    kind="line",
    marker="o",
    figsize=(10, 5)
)

pl.title("Monthly Sales Trend")
pl.xlabel("Month")
pl.ylabel("Sales")

pl.grid(True)

pl.tight_layout()
pl.savefig("IMAGES/monthly_sales.png")
pl.show()

# =========================================
# YEARLY SALES TREND
# =========================================

yearly_sales = (
    df.groupby("Year")["Sales"]
    .sum()
)

print("\nYearly Sales")
print(yearly_sales)

yearly_sales.plot(
    kind="line",
    marker="o",
    figsize=(10, 5)
)

pl.title("Yearly Sales Performance")
pl.xlabel("Year")
pl.ylabel("Sales")

pl.grid(True)

pl.tight_layout()
pl.savefig("IMAGES/yearly_sales.png")
pl.show()

# =========================================
# TOP CUSTOMERS
# =========================================

top_customers = (
    df.groupby("Customer Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop 10 Customers")
print(top_customers.head(10))

top_customers.head(10).plot(
    kind="bar",
    figsize=(14, 6)
)

pl.title("Top 10 Customers")
pl.xlabel("Customer Name")
pl.ylabel("Sales")

pl.tight_layout()
pl.savefig("IMAGES/top_customers.png")
pl.show()

# =========================================
# PROFIT ANALYSIS
# =========================================

profit_category = (
    df.groupby("Category")["Profit"]
    .sum()
)

profit_category.plot(
    kind="bar",
    figsize=(8, 5)
)

pl.title("Profit by Category")
pl.xlabel("Category")
pl.ylabel("Profit")

pl.tight_layout()
pl.savefig("IMAGES/profit_category.png")
pl.show()

# =========================================
# KPI METRICS
# =========================================

print("\n========== KPI METRICS ==========")

print("Total Sales:", round(df["Sales"].sum(), 2))
print("Total Profit:", round(df["Profit"].sum(), 2))
print("Total Orders:", df["Order ID"].nunique())
print("Total Customers:", df["Customer Name"].nunique())
print("Average Sales:", round(df["Sales"].mean(), 2))
print("Total Categories:", df["Category"].nunique())

# =========================================
# HEATMAP
# =========================================

pl.figure(figsize=(10, 6))

sns.heatmap(
    df.select_dtypes(include="number").corr(),
    annot=True,
    cmap="coolwarm"
)

pl.title("Correlation Heatmap")

pl.tight_layout()
pl.savefig("IMAGES/correlation_heatmap.png")
pl.show()

# =========================================
# SALES VS PROFIT
# =========================================

pl.figure(figsize=(8, 6))

sns.scatterplot(
    data=df,
    x="Sales",
    y="Profit"
)

pl.title("Sales vs Profit")

pl.tight_layout()
pl.savefig("IMAGES/sales_vs_profit.png")
pl.show()

# =========================================
# STACKED BAR CHART
# =========================================

stacked_data = df.pivot_table(
    values="Sales",
    index="Year",
    columns="Category",
    aggfunc="sum"
)

stacked_data.plot(
    kind="bar",
    stacked=True,
    figsize=(12, 6)
)

pl.title("Yearly Category Sales")
pl.xlabel("Year")
pl.ylabel("Sales")

pl.tight_layout()
pl.savefig("IMAGES/stacked_sales_chart.png")
pl.show()

print("\nAdvanced Visualizations Added Successfully")