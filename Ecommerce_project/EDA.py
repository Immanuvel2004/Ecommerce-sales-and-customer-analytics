import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("ecommerce_sales_34500.csv")

df["category"] = (
    df["category"]
    .str.strip()
    .str.lower()
)

df["order_date"]=pd.to_datetime(df["order_date"],errors="coerce")
df["year"] = df["order_date"].dt.year
df["month"] = df["order_date"].dt.month
df["month_name"] = df["order_date"].dt.month_name()
df["day"] = df["order_date"].dt.day
df["day_name"] = df["order_date"].dt.day_name()

df["revenue"] = df["price"] * df["quantity"]
df["discount_amount"] = (
    df["price"] *
    df["quantity"] *
    df["discount"] / 100
)
df["net_sales"] = (
    df["revenue"] - df["discount_amount"]
)

df.to_csv("Ecommerce_sales_cleaned.csv")