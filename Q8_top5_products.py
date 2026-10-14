import pandas as pd

sales_data = pd.DataFrame({
    "Product": ["Headphones", "Charger", "Phone Case", "Smartwatch", "Charger",
                "Power Bank", "Headphones", "USB Cable", "Phone Case", "Speaker",
                "Charger", "USB Cable"],
    "QuantitySold": [15, 20, 12, 8, 18, 10, 9, 25, 14, 6, 11, 7]
})

# Add up the quantity of each product, then take the 5 largest
product_totals = sales_data.groupby("Product")["QuantitySold"].sum()
top_5 = product_totals.nlargest(5)

print("Top 5 products sold in the past month:")
print(top_5.to_string())
