# DREVOL Internship Task 02

This repository contains the solutions for Task 02 of my internship at DREVOL. The task involves creating an SQL Order table, writing C#/.NET or Python code to display all orders, and using a predictive model for sales forecasting and customer behavior analysis.

## Task Overview

Task 02 is divided into three parts:

1. **SQL Order Table Creation:**
   - Create an SQL table named `Orders` with the following columns:
     - `Order_PK` (Primary Key)
     - `Customer_Number`
     - `Item_Number`
     - `Quantity`
     - `Price`

2. **Code Implementation:**
   - Develop C#/.NET or Python code to display all orders stored in the `Orders` table.

3. **Predictive Modeling:**
   - Use an existing model to predict:
     - Item-wise sales for the next month.
     - Customer behavior

## Requirements

- SQL Database (e.g., MySQL, PostgreSQL)
- C#/.NET or Python 3.x
- Libraries:
  - For C#: `System.Data.SqlClient`, `Dapper`, etc.
  - For Python: `pandas`, `mysql`, `sklearn`, etc.

## Project Structure

```bash
DREVOL-Task02/
├── sql/
│   └── create_orders_table.sql   # SQL script to create the Orders table
├── code/
│   ├── display_orders.py         # Python code to display orders
│   └── display_orders.cs         # C# code to display orders
├── models/
│   └── prediction_model.py       # Python script for sales prediction and customer behavior analysis
└── README.md
