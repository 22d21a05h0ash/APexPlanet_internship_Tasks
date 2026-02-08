# House Price Data Cleaning Project

This project demonstrates the process of **data exploration, cleaning, and preparation** for analysis using a house price dataset.  
The goal is to create a **clean, analysis-ready dataset** by handling missing values, duplicates, and adding a useful feature.

---

## Project Structure

HousePriceProject/
┣ raw_house_data.csv # Original dataset
┣ cleaned_house_data.csv # Cleaned dataset ready for analysis
┣ data_cleaning.py # Python script to clean the dataset
┣ data_dictionary.md # Description of all columns
┣ README.md # Project overview (this file)


---

## Dataset Description

The dataset contains information about houses, including size, number of rooms, location, year built, and sale price.

- **SquareFeet**: Area of the house in square feet  
- **Bedrooms**: Number of bedrooms  
- **Bathrooms**: Number of bathrooms  
- **Neighborhood**: Area / location of the house (Urban, Suburb, Rural)  
- **YearBuilt**: Year the house was built  
- **Price**: Sale price of the house  

---

## Steps Performed

1. **Data Exploration**
   - Loaded the dataset using Pandas  
   - Viewed the first few rows using `df.head()`  
   - Checked data types and basic statistics using `df.info()` and `df.describe()`  

2. **Data Quality Assessment**
   - Checked for missing values in each column using `df.isnull().sum()`  
   - Checked for duplicate rows using `df.duplicated().sum()`  

3. **Data Cleaning**
   - Removed duplicate rows with `df.drop_duplicates()`  
   - Filled missing numeric values with median (e.g., `Bedrooms`, `Bathrooms`)  
   - Filled missing categorical values with `'Unknown'` (e.g., `Neighborhood`)  

4. **Feature Engineering**
   - Added a new column `HouseAge` calculated as `current_year - YearBuilt`  
   - This feature represents the age of the house in years and is useful for analysis  

5. **Save Cleaned Data**
   - Saved the cleaned dataset as `cleaned_house_data.csv`  

---

## Tools Used

- **Python 3**  
- **Pandas** for data handling  
- **Datetime** for calculating `HouseAge`  

---

## Outcome

- Original dataset: `raw_house_data.csv`  
- Cleaned and ready-to-analyze dataset: `cleaned_house_data.csv`  
- Data cleaning script: `data_cleaning.py`  
- Data dictionary: `data_dictionary.md`  

The project demonstrates the ability to **explore, clean, and prepare data** for analysis, which is a critical first step in any data analytics workflow.

---

## Optional Next Steps

- Perform **data visualization** to understand price trends by neighborhood, house size, or age  
- Feed the cleaned dataset into a **machine learning model** for price prediction
