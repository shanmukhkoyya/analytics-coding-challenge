# Food Delivery SQL Case | Day 01

**Scenario:** You are analysing customer and restaurant activity for an online food-delivery platform.  
**Database:** MySQL · **Level:** SQL fundamentals to intermediate querying

## The business question

Which customers order and spend the most, which restaurants receive the most orders, and how does activity vary by city and date?

## Data model

### Customers

| Field | Description |
|---|---|
| customer_id | Customer identifier |
| name | Customer name |
| city | Customer city |

### Orders

| Field | Description |
|---|---|
| order_id | Order identifier |
| customer_id | Customer reference |
| restaurant | Restaurant name |
| amount | Order amount |
| order_date | Order date |

The Orders table is linked to Customers through customer_id.

## Query brief

The SQL script answers ten business questions:

1. Find customers who have ordered.
2. Calculate total spend for each customer.
3. Identify the top three customers by spend.
4. Find orders in the seven days before the latest order date.
5. Find customers who have never ordered.
6. Identify the restaurant with the most orders.
7. Find Bengaluru customers spending more than ₹1,000.
8. Count orders by city.
9. Calculate average order amount by restaurant.
10. Identify customers with more than five orders.

Five additional interview-practice queries cover platform revenue, average order value, unique ordering customers, customer order summaries and the highest-value order.

## SQL methods used

SELECT · DISTINCT · WHERE · ORDER BY · LIMIT · INNER JOIN · LEFT JOIN · GROUP BY · HAVING · SUM · COUNT · AVG · ROUND · subqueries · DATE_SUB · COUNT(DISTINCT)

## Files

- [Main SQL script](Day-01-SQL-Food-Delivery-Analysis.sql) — database setup, sample rows, ten business queries and five interview exercises.
- [Challenge PDF](Coding%20Challenge-Day%201.pdf) — original project brief.

## Run safely

1. Open the SQL script in MySQL Workbench or another MySQL client.
2. Review the database and table setup before execution.
3. Run the script in order, using a practice database.
4. The script recreates only the Orders and Customers tables in the DAY1 database; existing rows in those two project tables will be replaced.
5. Run the analysis queries individually and inspect each result.

## Interpretation

The included records are practice data. They demonstrate SQL query patterns and should not be treated as real food-delivery business performance.

---

**Day 01 of the Data Analytics Coding Challenge**  
Shanmukh Koyya · [GitHub](https://github.com/shanmukhkoyya) · [LinkedIn](https://www.linkedin.com/in/shanmukh-koyya/)
