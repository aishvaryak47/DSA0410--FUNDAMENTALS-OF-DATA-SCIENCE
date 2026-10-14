import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales = [42000, 38000, 45000, 51000, 49000, 56000,
         60000, 58000, 63000, 67000, 72000, 80000]

# 1. Line plot
plt.figure(figsize=(9, 5))
plt.plot(months, sales, marker="o", color="tab:blue", linewidth=2)
plt.title("Monthly Sales - Line Plot")
plt.xlabel("Month")
plt.ylabel("Sales (Rs.)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()

# 2. Bar plot
plt.figure(figsize=(9, 5))
plt.bar(months, sales, color="tab:orange")
plt.title("Monthly Sales - Bar Plot")
plt.xlabel("Month")
plt.ylabel("Sales (Rs.)")
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.show()
