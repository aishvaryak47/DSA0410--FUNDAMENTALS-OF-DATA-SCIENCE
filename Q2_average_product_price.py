import numpy as np

# 3x3 matrix: each row = a product, each column = the price it sold at in one sale this month
sales = np.array([
    [250.0, 260.0, 245.0],   # Product A
    [120.0, 115.0, 125.0],   # Product B
    [499.0, 510.0, 489.0]    # Product C
])
products = ["Product A", "Product B", "Product C"]

avg_per_product = np.mean(sales, axis=1)
for product, avg in zip(products, avg_per_product):
    print(f"Average price of {product}: Rs. {avg:.2f}")

overall_avg = np.mean(sales)
print(f"Average price of all products sold: Rs. {overall_avg:.2f}")
