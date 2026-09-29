import pandas as pd
from sqlalchemy import create_engine

# -----------------------------------
# SQL SERVER CONNECTION
# -----------------------------------

server = "localhost"
database = "ECommerce_OLTP"

connection_string = (
    "mssql+pyodbc://@"
    + server
    + "/"
    + database
    + "?driver=ODBC+Driver+18+for+SQL+Server"
    + "&trusted_connection=yes"
    + "&TrustServerCertificate=yes"
)

engine = create_engine(connection_string)

# -----------------------------------
# EXCEL FILE
# -----------------------------------

excel_file = "ecommerce_powerbi_practice.xlsx"

# Read Excel sheets
categories = pd.read_excel(excel_file, sheet_name="Categories")
customers = pd.read_excel(excel_file, sheet_name="Customers")
products = pd.read_excel(excel_file, sheet_name="Products")
orders = pd.read_excel(excel_file, sheet_name="Orders")
order_items = pd.read_excel(excel_file, sheet_name="Order_Items")
payments = pd.read_excel(excel_file, sheet_name="Payments")

# -----------------------------------
# DISPLAY ROW COUNTS
# -----------------------------------

print("Excel data loaded:")
print("Categories:", len(categories))
print("Customers:", len(customers))
print("Products:", len(products))
print("Orders:", len(orders))
print("Order Items:", len(order_items))
print("Payments:", len(payments))

# -----------------------------------
# LOAD DATA INTO SQL SERVER
# -----------------------------------

print("\nLoading data into SQL Server...")

categories.to_sql(
    "Categories",
    engine,
    if_exists="append",
    index=False
)

customers.to_sql(
    "Customers",
    engine,
    if_exists="append",
    index=False
)

products.to_sql(
    "Products",
    engine,
    if_exists="append",
    index=False
)

orders.to_sql(
    "Orders",
    engine,
    if_exists="append",
    index=False
)

order_items.to_sql(
    "OrderItems",
    engine,
    if_exists="append",
    index=False
)

payments.to_sql(
    "Payments",
    engine,
    if_exists="append",
    index=False
)

print("\nSUCCESS!")
print("Excel data has been loaded into SQL Server.")