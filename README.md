# E-Commerce Sales Analysis Hackathon
BY JUANITA CHEPHCUMBA
## 🏆 Project Overview
This project is part of the **E-Commerce Sales Analysis Hackathon**, where the goal is to analyze sales data to uncover valuable insights on customer behavior, sales trends, and order fulfillment efficiency. The analysis is conducted using **SQL, Python, and Power BI**.

---

## 🔎 Hackathon Questions
The analysis is guided by the following key questions:

### **Sales Analysis**
1️⃣ What are the **total sales by region**?
2️⃣ Which **product category** generates the highest revenue?
3️⃣ What is the **average shipping fee** by region?

### **Customer Behavior**
4️⃣ How does **customer age** impact purchasing behavior?
5️⃣ What is the **most popular product by gender**?

### **Order Fulfillment**
6️⃣ What is the **order fulfillment rate** (delivered vs. returned)?
7️⃣ Are there **trends in shipping status over time**?

---

## 📂 Project Structure
- **Files/** → Contains SQL, Python, and Power BI analysis files.
  - `SQL_Analysis_Queries.sql` → SQL queries for sales insights.
  - `Python_Analysis_Scripts.ipynb` → Python scripts for data processing.
  - `PowerBI_Analysis_Dashboard.pbix` → Power BI dashboard file.
- **img/** → Contains visualization screenshots.
- **sales_data.csv** → The dataset used for analysis.
- **README.md** → This documentation file.

---

## 📊 Data Analysis Process

### **1️⃣ Data Cleaning Process**
- Removed missing values and duplicates.
- Standardized data types.
- Converted `OrderDate` into a datetime format.

### **2️⃣ SQL Analysis**
Performed SQL queries to extract insights:

#### ✅ Total Sales by Region
![Sales by Region](img/Image1.PNG)

#### ✅ Highest Revenue-Generating Category
![Top Product Category](img/Image2.PNG)

#### ✅ Average Shipping Fee by Region
![Shipping Fee](img/Image3.PNG)

#### ✅ Customer Age vs. Purchasing Behavior
![Customer Age](img/Image4.1.PNG) ![Customer Age](img/Image4.2.PNG) ![Customer Age](img/Image4.3.PNG)

#### ✅ Most Popular Product by Gender
![Popular Product](img/Image5.PNG)

#### ✅ Order Fulfillment Rate
![Order Fulfillment](img/Image6.PNG)

---

## 🐍 Python Analysis

### **1️⃣ Installing Dependencies & Connecting to the Database**
The Python analysis was performed using **Pandas and SQLAlchemy** to process sales data.

### **2️⃣ Data Cleaning & Preprocessing**
- Handled missing values and duplicates.
- Transformed data into structured formats for analysis.

![Data Loading](img/Image7.PNG)<br>
![Data Cleaning](img/Image8.PNG)

### **3️⃣ Exploratory Data Analysis (EDA)**
- **Total Sales by Category** → Analyzed revenue per product type.<br>
![Total Sales by category](img/Image9.PNG)<br>

- **Daily Sales Trends Over Time** → Identified peak shopping months.<br>
![Sales Trends over time](img/Image10.PNG)<br>

**Monthly Sales Trends Over Time** → Identified peak shopping months.<br>
![Sales Trends over time](img/Image12.PNG)<br>

- **Customer Spending Trends** → Gender-based and region-based analysis.<br>
![Agerage spending per customer by gender](img/Image11.PNG)<br>
![Sales distribution by region](img/Image14.PNG)<br>

- **Order Delivery Status** → Analyzed delivery success rates.<br>
![Shipping status distribution](img/Image15.PNG)<br>

- **Python dashboard**<br>
![Dashboard](img/Image16.PNG)<br>
![Dashboard](img/Image175.PNG)

---

## 📈 Power BI Dashboard
# Power BI Analysis for E-Commerce Sales

## 📊 Overview
This document outlines the process of building a Power BI dashboard for the **E-Commerce Sales Analysis Hackathon**. The dashboard visualizes key insights from the dataset, including **sales trends, customer behavior, and order fulfillment metrics**.

---

## 🎯 Objectives
- Identify **top-selling products and high-revenue categories**.
- Analyze **sales trends over time** to determine peak shopping periods.
- Assess **customer demographics (gender, age, region) and their impact on purchasing behavior**.
- Evaluate the **order fulfillment rate** (delivered vs. returned orders).

---

## 📂 Dataset Used
- **File Name:** `sales_data.csv`
- **Key Columns:**
  - `CustomeNo`, `CustomerID`, `Gender`, `Age`, `Region`
  - `ProductName`, `Category`, `UnitPrice`, `Quantity`, `TotalPrice`
  - `ShippingStatus`, `OrderDate`

---

## 🛠️ Steps to Build the Dashboard

### **1️⃣ Data Import & Preparation**
- Imported `sales_data.csv` into Power BI.
- Checked data types and ensured correct formatting.
- Transformed `OrderDate` into **Date/Time format** for time-based analysis.
- Removed duplicate entries and handled missing values.

### **2️⃣ Data Cleaning & Transformation**
- Created **calculated columns**:
  - `TotalRevenue = UnitPrice * Quantity`
  - `AverageShippingFee = AVERAGE(ShippingFee)`
- Used **DAX (Data Analysis Expressions)** to compute revenue by category and region.

### **3️⃣ Creating Visualizations**
✅ **Total Sales Overview** → KPI Card displaying total sales.<br>
![Total Sales Overview](img/Image18.PNG)

✅ **Sales by Region** → Donut Chart showing revenue per region.<br>
![Sales by Region](img/Image21.PNG)

✅ **Sales by Category** → Pie Chart comparing delivered vs. returned orders.<br>
![Sales by Category](img/Image22.PNG)

✅ **Top-Selling Products** → Bar Chart ranking best-selling products.<br>
![Top Selling Products](img/Image20.PNG)

✅ **Sales Trend Over Time** → Line Chart tracking revenue over months.<br>
![Sales Trend](img/Image19.PNG)

✅ **Customer Demographics** → Gender-based & Age-based spending analysis.<br>
![Sales by Gender](img/Image23.PNG) <br>
![Sales by Age](img/Image24.PNG)

---

**DASHBOARD**
![Dashboard](img/Image25.PNG)

---

## 📌 Business Insights & Recommendations
📌 **Laptops & Smartphones** generate the highest revenue. Focus marketing efforts on these products.
📌 **North & East regions** drive the most sales. Consider expanding services in these areas.
📌 **Customers aged 45-54** spend the most. Personalized marketing can increase sales.
📌 **5% of orders are returned**, indicating potential issues with product quality or delivery service.

---

## 🎯 Conclusion
This analysis provides valuable insights into customer purchasing patterns, sales trends, and operational efficiency. These findings can be leveraged for **business decision-making, marketing strategies, and supply chain improvements**.

