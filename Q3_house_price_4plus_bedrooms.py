import numpy as np

# In the lab, load the CSV file like this:
# house_data = np.genfromtxt("house_data.csv", delimiter=",", skip_header=1)
# Columns: bedrooms, square footage, sale price
house_data = np.array([
    [3, 1500, 4500000],
    [5, 2400, 8200000],
    [4, 2000, 6500000],
    [6, 3100, 11000000],
    [2, 1100, 3200000],
    [5, 2600, 8800000]
])

bedrooms = house_data[:, 0]
prices = house_data[:, 2]

# Boolean mask keeps only houses with more than 4 bedrooms
selected_prices = prices[bedrooms > 4]

if selected_prices.size > 0:
    print("Houses with more than 4 bedrooms:", selected_prices.size)
    print(f"Average sale price: Rs. {np.mean(selected_prices):,.2f}")
else:
    print("No houses with more than 4 bedrooms.")
