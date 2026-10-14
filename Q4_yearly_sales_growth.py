import numpy as np

# Sales amount for Q1, Q2, Q3, Q4
sales_data = np.array([120000, 135000, 150000, 168000])

total_sales = np.sum(sales_data)
percent_increase = (sales_data[3] - sales_data[0]) / sales_data[0] * 100

print("Quarterly sales:", sales_data)
print(f"Total sales for the year: Rs. {total_sales:,}")
print(f"Percentage increase from Q1 to Q4: {percent_increase:.2f}%")
