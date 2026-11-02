<div align="center"><h1>🍔 ORDER DESK / FOOD DELIVERY</h1><p>DAY 01 · SQL CASE STUDY</p></div>

## Daily operations snapshot
<table><tr><td align="center"><h1>10</h1><sub>customers</sub></td><td align="center"><h1>10</h1><sub>orders</sub></td><td align="center"><h1>8</h1><sub>ordered</sub></td><td align="center"><h1>2</h1><sub>no order</sub></td></tr></table>

## Restaurant sales board
| INDICATOR | RESULT |
|---|---:|
| Total order value | 6,620 |
| Average order value | 662 |
| Top restaurant | Meghana Foods |
| Orders at top restaurant | 3 |

## Data relationship sketch
```mermaid
erDiagram
 CUSTOMERS ||--o{ ORDERS : places
 RESTAURANTS ||--o{ ORDERS : receives
```

## SQL investigation route
`CUSTOMERS + ORDERS → JOIN → FIND NON-ORDERING CUSTOMERS → GROUP BY RESTAURANT → SUM ORDER VALUE`

## Project files
- [SQL script](Day-01-SQL-Food-Delivery-Analysis.sql)
- [Challenge PDF](Coding%20Challenge-Day%201.pdf)

> The SQL workflow drops and recreates only Orders and Customers in the DAY1 database. Use a disposable practice database.

<sub>Small assignment dataset; not a live food-delivery operating report.</sub>