# 📊 Coding Challenge – Day 1 | SQL

## 📌 Overview

Day 1 of my **Daily Data Analytics Challenge** focuses on SQL-based analysis for an online food delivery platform.

The objective is to analyze customer and order data and answer practical business questions using SQL queries.

---

## 🏢 Business Scenario

Assume I am working as a **Data Analyst for an online food delivery platform**.

The business maintains customer information and food order information. The objective is to analyze this data and generate useful insights using SQL.

---

## 🗄️ Database Structure

### Customers

| Column | Data Type | Description |
|---|---|---|
| customer_id | INT | Unique customer identifier |
| name | VARCHAR(50) | Customer name |
| city | VARCHAR(50) | Customer city |

### Orders

| Column | Data Type | Description |
|---|---|---|
| order_id | INT | Unique order identifier |
| customer_id | INT | Customer identifier |
| restaurant | VARCHAR(50) | Restaurant name |
| amount | DECIMAL(10,2) | Order amount |
| order_date | DATE | Date of order |

The `Orders.customer_id` column is related to `Customers.customer_id` through a foreign key. :contentReference[oaicite:1]{index=1}

---

## 🎯 SQL Tasks

The challenge contains 10 practical SQL tasks:

1. List all customers who have placed at least one order.
2. Find the total amount spent by each customer.
3. Display the top 3 customers based on total spending.
4. Retrieve orders placed in the last 7 days from the latest order date.
5. Show customers who have never placed an order.
6. Find the restaurant with the highest number of orders.
7. Find Bengaluru customers who spent more than ₹1,000.
8. Show the total number of orders placed per city.
9. Find the average order amount for each restaurant.
10. Identify customers who placed more than 5 orders.

---

## 🛠️ Skills Practiced

- `SELECT`
- `DISTINCT`
- `WHERE`
- `INNER JOIN`
- `LEFT JOIN`
- `GROUP BY`
- `HAVING`
- `ORDER BY`
- `LIMIT`
- Aggregate functions
  - `SUM()`
  - `COUNT()`
  - `AVG()`
- Subqueries
- `DATE_SUB()`
- Foreign Keys
- Customer and order analysis

---

## 📈 Analysis Covered

The queries analyze:

- Customer ordering behavior
- Customer spending
- Top customers
- Recent orders
- Inactive customers
- Restaurant order volume
- City-level order activity
- Restaurant-level average order value
- High-frequency customers

---

## 💡 Key Learning

This challenge helped strengthen my understanding of using SQL to solve practical business questions involving:

**Filtering → Joining → Aggregating → Grouping → Ranking → Business Analysis**

---

## 📂 Files

```text
Day-01/
│
├── Coding Challenge – Day 1(SQL).sql
└── README.md
