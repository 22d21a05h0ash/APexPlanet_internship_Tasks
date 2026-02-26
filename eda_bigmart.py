# ==========================================
# BIGMART SALES ANALYSIS - EDA PROJECT
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# STEP 1: Load Dataset
# -------------------------------
df = pd.read_csv("bigmart.csv")

print("\nFirst 5 Rows:")
print(df.head())

# -------------------------------
# STEP 2: Understand Data
# -------------------------------
print("\nDataset Shape:", df.shape)

print("\nColumn Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# -------------------------------
# STEP 3: Handle Missing Values
# -------------------------------

# Fill Item_Weight with mean
df['Item_Weight'].fillna(df['Item_Weight'].mean(), inplace=True)

# Fill Outlet_Size with mode
df['Outlet_Size'].fillna(df['Outlet_Size'].mode()[0], inplace=True)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# -------------------------------
# STEP 4: Sales Distribution
# -------------------------------
plt.figure(figsize=(6,4))
plt.hist(df['Item_Outlet_Sales'], bins=30)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Count")
plt.savefig("sales_distribution.png")  # Save Image
plt.show()

# -------------------------------
# STEP 5: Item Category Analysis
# -------------------------------
plt.figure(figsize=(10,5))
df['Item_Type'].value_counts().plot(kind='bar')
plt.title("Items per Category")
plt.xlabel("Item Type")
plt.ylabel("Count")
plt.savefig("item_category.png")  # Save Image
plt.show()

# -------------------------------
# STEP 6: Business Analysis
# -------------------------------
print("\nTop Selling Item Types:")
print(df.groupby('Item_Type')['Item_Outlet_Sales'].sum().sort_values(ascending=False))

print("\nSales by Outlet Type:")
print(df.groupby('Outlet_Type')['Item_Outlet_Sales'].sum())

print("\nSales by Location:")
print(df.groupby('Outlet_Location_Type')['Item_Outlet_Sales'].sum())

# -------------------------------
# STEP 7: Price vs Sales Relationship
# -------------------------------
plt.figure(figsize=(6,4))
plt.scatter(df['Item_MRP'], df['Item_Outlet_Sales'])
plt.xlabel("Item MRP")
plt.ylabel("Sales")
plt.title("Price vs Sales Relationship")
plt.savefig("price_vs_sales.png")  # Save Image
plt.show()

# -------------------------------
# STEP 8: Correlation Heatmap
# -------------------------------
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Correlation Heatmap")
plt.savefig("correlation_heatmap.png")  # Save Image
plt.show()

print("\nEDA Completed Successfully ✅")
print("Images saved in project folder.")