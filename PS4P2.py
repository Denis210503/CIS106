price_per_share = float(
    input("Price per share at the moment of transaction : "))
current_stock_price = float(input("Enter the current stock price: "))
quantity_of_stock = float(input("Enter the quantity of stock: "))
total = (current_stock_price - price_per_share) * quantity_of_stock
if total > 0:
  print("After the transaction, you gained $", total)
elif total < 0:
  print("After the transaction, you lost $", total)
else:
  print("After the transaction, you broke even")

