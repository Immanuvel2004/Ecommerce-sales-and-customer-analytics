# 🛒 E-Commerce Sales & Customer Analytics Dashboard

## 📊 Project Overview

An end-to-end e-commerce analytics project designed to transform raw Excel
transactional data into actionable business insights using Python, Pandas,
SQL Server, Power BI, Power Query, and DAX.

The project covers the complete data analytics workflow including data
cleaning, transformation, database loading, data modeling, KPI development,
and interactive Power BI dashboard development.

---

## 🎯 Business Objectives

The project helps answer:

- How are overall sales and profitability performing?
- What are the monthly sales trends?
- Which product categories generate the most revenue?
- Which products are top performers?
- Which products generate the highest profit?
- Which customers contribute the most revenue?
- What is the average order value?
- How profitable are different product categories?
- What is the relationship between discounting and profitability?
- How does customer behavior vary across the business?

---

## 🏗️ Architecture

Excel Raw Data
        ↓
Python / Pandas
        ↓
Data Cleaning & Transformation
        ↓
SQL Server
        ↓
Data Validation & Analysis
        ↓
Power BI
        ↓
Data Modeling
        ↓
DAX Measures
        ↓
Interactive Business Dashboard

---

## 🐍 Data Cleaning & Transformation

Python and Pandas were used to clean and transform the raw Excel dataset
before loading it into SQL Server.

The data preparation process included:

- Handling missing values
- Removing duplicate records
- Standardizing column names
- Converting data types
- Formatting date fields
- Cleaning categorical values
- Validating numerical fields
- Transforming raw data into an analysis-ready format

---

## 🗄️ SQL Server Database

The cleaned and transformed data was loaded into SQL Server using Python.

The database contains a relational structure with:

- Customers
- Orders
- OrderItems
- Products
- Categories
- Payments

Key relationships connect customers, orders, products, categories,
order items, and payment information.

---

## 🔗 SQL Server → Power BI

The processed data was connected from SQL Server to Power BI.

Power BI was used to build the analytical data model, create DAX measures,
and develop interactive business dashboards.

---

## 📊 Power BI Dashboard

The Power BI report contains four analytical pages.

---

### 1. Executive Dashboard

Provides a high-level overview of overall business performance.

KPIs:

- Total Sales
- Total Profit
- Total Orders
- Total Customers
- Average Order Value
- Profit Margin %

Visualizations:

- Monthly Revenue Trend
- Monthly Profit Trend
- Sales by Category
- Sales by State
- Top Products
- Customer Performance

---

### 2. Sales Analysis

Analyzes sales trends and overall sales performance.

Includes:

- Total Sales
- Total Orders
- Total Quantity
- Average Order Value
- Monthly Sales Trend
- Sales by Category
- Sales by State
- Customer Segment Analysis
- Discount Analysis

---

### 3. Customer Analytics

Analyzes customer purchasing behavior and revenue contribution.

Includes:

- Total Customers
- Customer Revenue
- Top 10 Customers
- Customer Segmentation
- Returning Customer Analysis
- Purchase Behavior

---

### 4. Product & Category Analytics

Analyzes product and category performance.

Includes:

- Top 10 Products by Sales
- Top 10 Products by Profit
- Sales by Category
- Profit by Category
- Quantity Sold
- Discount vs Profit Analysis

---

## 🧮 DAX Measures

Key measures created:

```DAX
Total Sales =
SUM(OrderItems[SalesAmount])

Total Profit =
SUM(OrderItems[SalesAmount]) -
SUM(OrderItems[CostAmount])

Total Orders =
DISTINCTCOUNT(Orders[OrderID])

Total Customers =
DISTINCTCOUNT(Orders[CustomerID])

Total Quantity =
SUM(OrderItems[Quantity])

Average Order Value =
DIVIDE(
    [Total Sales],
    [Total Orders]
)

Profit Margin % =
DIVIDE(
    [Total Profit],
    [Total Sales]
)
