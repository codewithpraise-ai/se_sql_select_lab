# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")


# Display all employees
employee_data = pd.read_sql("""
SELECT * FROM employees
""", conn)

print("---------------------Employee Data---------------------")
print(employee_data)
print("-------------------End Employee Data-------------------")


# STEP 2
# Select employee number and last name
df_first_five = pd.read_sql("""
SELECT employeeNumber, lastName
FROM employees
""", conn)


# STEP 3
# Select last name followed by employee number
df_five_reverse = pd.read_sql("""
SELECT lastName, employeeNumber
FROM employees
""", conn)


# STEP 4
# Rename employeeNumber to ID
df_alias = pd.read_sql("""
SELECT lastName, employeeNumber AS ID
FROM employees
""", conn)


# STEP 5
# Categorize employees according to their job titles
df_executive = pd.read_sql("""
SELECT *,
    CASE
        WHEN jobTitle = 'President'
          OR jobTitle = 'VP Sales'
          OR jobTitle = 'VP Marketing'
        THEN 'Executive'
        ELSE 'Not Executive'
    END AS role
FROM employees
""", conn)


# STEP 6
# Find the length of each employee's last name
df_name_length = pd.read_sql("""
SELECT LENGTH(lastName) AS name_length
FROM employees
""", conn)


# STEP 7
# Extract the first two letters of each job title
df_short_title = pd.read_sql("""
SELECT SUBSTR(jobTitle, 1, 2) AS short_title
FROM employees
""", conn)


# STEP 8
# Calculate the sum of rounded order prices
# STEP 8
sum_total_price = pd.read_sql("""
    SELECT SUM(ROUND(priceEach * quantityOrdered)) AS total_price
    FROM orderdetails
""", conn).values[0]


# STEP 9
# Display the original order date and its day, month, and year
df_day_month_year = pd.read_sql("""
SELECT
    orderDate,
    SUBSTR(orderDate, 9, 2) AS day,
    SUBSTR(orderDate, 6, 2) AS month,
    SUBSTR(orderDate, 1, 4) AS year
FROM orders
""", conn)


# Close the database connection
conn.close()