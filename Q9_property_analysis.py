import pandas as pd

property_data = pd.DataFrame({
    "PropertyID": ["P101", "P102", "P103", "P104", "P105", "P106", "P107", "P108"],
    "Location": ["Anna Nagar", "Velachery", "Adyar", "Anna Nagar",
                 "Velachery", "Adyar", "Tambaram", "Tambaram"],
    "Bedrooms": [3, 2, 5, 4, 6, 3, 2, 5],
    "AreaSqFt": [1500, 1100, 2800, 2000, 3200, 1600, 950, 2400],
    "ListingPrice": [9500000, 6200000, 21000000, 13500000,
                     18500000, 11000000, 4200000, 8900000]
})

# 1. Average listing price in each location
avg_price = property_data.groupby("Location")["ListingPrice"].mean()
print("1. Average listing price per location:")
print(avg_price.to_string())

# 2. Number of properties with more than four bedrooms
count_big = (property_data["Bedrooms"] > 4).sum()
print("\n2. Properties with more than 4 bedrooms:", count_big)

# 3. Property with the largest area
largest = property_data.loc[property_data["AreaSqFt"].idxmax()]
print("\n3. Property with the largest area:")
print(largest.to_string())
