def read_order_data(file_path):
  orders = []
  with open(file_path, 'r') as file:
      lines = file.readlines()
      for i in range(0, len(lines), 3):
          item = lines[i].strip()
          quantity = int(lines[i + 1].strip())
          price = float(lines[i + 2].strip())
          orders.append((item, quantity, price))
  return orders

def calculate_extended_prices(orders):
  total_extended_price = 0
  for item, quantity, price in orders:
      extended_price = quantity * price
      total_extended_price += extended_price
      print(f"Item: {item}, Quantity: {quantity}, Price: {price:.2f}, Extended Price: {extended_price:.2f}")
  return total_extended_price

def main():
  file_path = 'order_data.txt'
  orders = read_order_data(file_path)
  total_extended_price = calculate_extended_prices(orders)
  order_count = len(orders)
  average_order = total_extended_price / order_count if order_count > 0 else 0

  print(f"\nTotal Extended Prices: {total_extended_price:.2f}")
  print(f"Number of Orders: {order_count}")
  print(f"Average Order: {average_order:.2f}")

if __name__ == "__main__":
  main()
