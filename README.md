# 🛒 BigMart Sales Data Analysis

## 📌 Project Overview

This project analyzes the **BigMart Sales Dataset** to uncover insights about product performance, outlet characteristics, and factors influencing sales.
The workflow combines **Python (EDA)**, **SQL (business queries)**, and **Data Visualization** to simulate a real-world data analyst task.

---

## 🎯 Objective

* Clean and explore retail data
* Answer business questions using SQL
* Identify trends affecting sales
* Present insights through visualizations and a dashboard

---

## 🧰 Tools & Technologies Used

* **Python** → Data Cleaning & EDA
* **Pandas, Matplotlib, Seaborn** → Data Analysis & Visualization
* **SQLite / SQL** → Business Querying
* **Jupyter Notebook** → Development Environment
* **PowerPoint** → Final Dashboard Presentation

---

## 📂 Project Structure

```
BigMart-Analysis/
│
├── data/
│   └── bigmart.csv
│
├── eda_bigmart.py
├── bigmart_queries.sql
├── outputs/
│   ├── sales_by_outlet.png
│   ├── item_type_distribution.png
│   └── mrp_vs_sales.png
│
├── BigMart_Analysis_Presentation.pptx
└── README.md
```

---

## 🔍 Workflow Followed

### STEP 1 — Data Collection

Used the BigMart dataset containing:

* 8,523 rows
* 12 features (Product, Outlet, Sales information)

---

### STEP 2 — Data Cleaning (EDA)

Handled:

* Missing values in `Item_Weight` and `Outlet_Size`
* Standardized categorical values
* Checked distributions and statistical summaries

---

### STEP 3 — SQL Analysis

Business-style questions answered:

* Which outlet type generates the highest sales?
* Which item categories sell the most?
* How does location affect revenue?
* What is the average sales by outlet size?

---

### STEP 4 — Data Visualization

Created charts to show:

* Sales by Outlet Type
* Item Category Distribution
* MRP vs Sales Relationship

(Stored inside the **outputs/** folder)

---

### STEP 5 — Dashboard Presentation

Summarized:

* Key Insights
* Business Impact
* Recommendations

---

## 📊 Key Insights

✔ Supermarket Type1 contributes the highest total sales
✔ Item MRP strongly influences sales performance
✔ Medium-size outlets perform more consistently
✔ Certain product categories dominate revenue share

---

## ▶️ How to Run This Project

### 1️⃣ Install Required Libraries

```bash
pip install pandas matplotlib seaborn sqlite3
```

### 2️⃣ Run EDA Script

```bash
python eda_bigmart.py
```

### 3️⃣ Execute SQL Queries

Open:

```
bigmart_queries.sql
```

Run queries using SQLite / DB Browser.

### 4️⃣ View Outputs

Check generated charts inside:

```
outputs/
```

---

## 📈 Deliverables

* Cleaned dataset
* SQL analysis queries
* Visualizations
* Presentation dashboard

---

## 🙋‍♀️ Author

**Ashwitha Rendla**
Computer Science Undergraduate | Aspiring Data Analyst

---

## ⭐ If You Like This Project

Give it a star on GitHub and feel free to connect!
