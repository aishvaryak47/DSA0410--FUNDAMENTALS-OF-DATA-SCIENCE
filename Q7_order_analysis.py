import pandas as pd

order_data = pd.DataFrame({
    "CustomerID": [101, 102, 101, 103, 102, 101, 104, 103],
    "OrderDate": ["2026-09-02", "2026-09-05", "2026-09-10", "2026-09-12",
                  "2026-09-15", "2026-09-20", "2026-09-22", "2026-09-28"],
    "ProductName": ["Laptop", "Mouse", "Keyboard", "Laptop",
                    "Monitor", "Mouse", "Keyboard", "Mouse"],
    "OrderQuantity": [1, 3, 2, 1, 2, 4, 1, 2]
})
order_data["OrderDate"] = pd.to_datetime(order_data["OrderDate"])

# 1. Total number of orders made by each customer
orders_per_customer = order_data.groupby("CustomerID").size()
print("1. Total orders per customer:")
print(orders_per_customer.to_string())

# 2. Average order quantity for each product
avg_quantity = order_data.groupby("ProductName")["OrderQuantity"].mean()
print("\n2. Average order quantity per product:")
print(avg_quantity.to_string())

# 3. Earliest and latest order dates
print("\n3. Earliest order date:", order_data["OrderDate"].min().date())
print("   Latest order date:  ", order_data["OrderDate"].max().date())
