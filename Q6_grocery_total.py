prices = [45.0, 120.0, 30.0, 250.0]   # price of each item
quantities = [2, 1, 5, 1]             # quantity of each item
discount_rate = 10                    # percent
tax_rate = 5                          # percent

subtotal = 0
for price, qty in zip(prices, quantities):
    subtotal += price * qty

discount = subtotal * discount_rate / 100
after_discount = subtotal - discount
tax = after_discount * tax_rate / 100
total_cost = after_discount + tax

print(f"Subtotal: Rs. {subtotal:.2f}")
print(f"Discount ({discount_rate}%): -Rs. {discount:.2f}")
print(f"Amount after discount: Rs. {after_discount:.2f}")
print(f"Tax ({tax_rate}%): +Rs. {tax:.2f}")
print(f"Total cost: Rs. {total_cost:.2f}")
