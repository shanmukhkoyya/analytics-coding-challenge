# 📊 Day 01 — SQL Food Delivery Analysis

## 📌 Project Overview

Day 01 of the **Data Analytics Coding Challenge** focuses on using **MySQL / SQL** to analyze customer and food-order data for an online food delivery platform.

The goal is to answer practical business questions using SQL and strengthen core Data Analyst skills such as **joins, aggregation, filtering, grouping, subqueries, date analysis, and business-oriented querying**.

---

## 🏢 Business Scenario

Assume I am working as a **Data Analyst for an online food delivery platform**.

The platform stores customer information, customer location, restaurant information, order amounts, and order dates.

The analysis is designed to answer questions about **customer spending, ordering behavior, restaurant performance, and city-level activity**.

---

## 🗄️ Database Structure

### Customers

| Column | Data Type | Description |
|---|---|---|
| `customer_id` | INT | Unique customer identifier |
| `name` | VARCHAR(50) | Customer name |
| `city` | VARCHAR(50) | Customer city |

### Orders

| Column | Data Type | Description |
|---|---|---|
| `order_id` | INT | Unique order identifier |
| `customer_id` | INT | Customer identifier |
| `restaurant` | VARCHAR(50) | Restaurant name |
| `amount` | DECIMAL(10,2) | Order amount |
| `order_date` | DATE | Order date |

### Relationship

`Orders.customer_id` is connected to `Customers.customer_id` through a foreign-key relationship.

---

## 🎯 Business Questions

The SQL analysis answers these 10 practical questions:

1. Which customers have placed at least one order?
2. How much has each customer spent?
3. Who are the top 3 customers by total spending?
4. Which orders fall within the last 7 days of the latest order date?
5. Which customers have never placed an order?
6. Which restaurant received the highest number of orders?
7. Which Bengaluru customers spent more than ₹1,000?
8. How many orders were placed from each city?
9. What is the average order amount for each restaurant?
10. Which customers placed more than 5 orders?

---

## 🧠 SQL Concepts Practiced

### Core SQL
- `SELECT`
- `DISTINCT`
- `WHERE`
- `ORDER BY`
- `LIMIT`

### Joins
- `INNER JOIN`
- `LEFT JOIN`
- Foreign-key relationships

### Aggregation
- `SUM()`
- `COUNT()`
- `AVG()`
- `ROUND()`

### Grouping & Filtering
- `GROUP BY`
- `HAVING`

### Advanced Querying
- Subqueries
- `DATE_SUB()`
- `COUNT(DISTINCT ...)`

---

## 💼 Interview Practice

Additional queries were added to practice common Data Analyst interview questions:

- Total platform revenue
- Average order value
- Number of unique ordering customers
- Customer order count and total spending
- Highest-value order

This extends the challenge beyond the original 10 business questions and provides additional SQL practice for interviews.

---

## 📈 Analysis Areas

**Customer Analysis**
- Customer spending
- Order frequency
- Active vs. inactive customers
- High-value customers

**Restaurant Analysis**
- Order volume
- Average order amount
- Highest-value orders

**Geographic Analysis**
- Orders by city
- Bengaluru customer spending

**Time Analysis**
- Recent orders using the latest order date as the reference point

---

## 🛠️ Tools Used

- **MySQL**
- **SQL**
- **Git**
- **GitHub**

---

## 📂 Files

```text
Day-01-SQL-Food-Delivery-Analysis/
│
├── Day-01-SQL-Food-Delivery-Analysis
├── Coding Challenge-Day 1.pdf
└── README.md
```

The SQL file contains:

- Database and table creation
- Sample data insertion
- Data inspection queries
- 10 business analysis questions
- 5 additional interview-practice queries

---

## 🔍 How to Run

1. Open **MySQL Workbench** or another MySQL client.
2. Open the SQL file in this folder.
3. Execute the script from top to bottom.
4. Select the `DAY1` database.
5. Run the business and interview queries individually to inspect the results.

---

## 🎓 Key Learning

This challenge strengthened the practical SQL workflow:

**Understand the data → Join tables → Filter records → Aggregate metrics → Group results → Apply business conditions → Interpret the output**

---

## 👤 Author

**Shanmukh Koyya**  
AI Data Analyst — Portfolio & Interview Practice

📧 **Email:** [shanmukhkoyya1234@gmail.com](mailto:shanmukhkoyya1234@gmail.com)  
🔗 **LinkedIn:** [linkedin.com/in/shanmukh-koyya](https://www.linkedin.com/in/shanmukh-koyya/)  
💻 **GitHub:** [github.com/shanmukhkoyya](https://github.com/shanmukhkoyya)

Skills developed across this coding challenge include **SQL, Excel, Power BI, DAX and Python**.