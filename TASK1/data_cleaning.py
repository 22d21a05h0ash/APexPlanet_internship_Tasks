import pandas as pd
from datetime import datetime

# Load the CSV file
df = pd.read_csv("raw_house_data.csv")

# Show first 5 rows
print(df.head())

# Check missing values
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Fill missing numeric values
df['Bedrooms'] = df['Bedrooms'].fillna(df['Bedrooms'].median())
df['Bathrooms'] = df['Bathrooms'].fillna(df['Bathrooms'].median())

# Fill missing text values
df['Neighborhood'] = df['Neighborhood'].fillna('Unknown')

# Feature engineering: HouseAge
current_year = datetime.now().year
df['HouseAge'] = current_year - df['YearBuilt']

# Save the cleaned dataset
df.to_csv("cleaned_house_data.csv", index=False)
print("Cleaning done with HouseAge added!")
