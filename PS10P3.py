def compute_discount(quantity, price, discount_rate):
  total_price = quantity * price
  discount_amount = total_price * (discount_rate / 100)
  discounted_price = total_price - discount_amount
  return discount_amount, discounted_price

def main():
  while True:
      continue_program = input("Do you want to do this program (Yes or No)? ").strip().lower()
      if continue_program != 'yes':
          break

      try:
          quantity = int(input("Enter the quantity: "))
          price = float(input("Enter the price per item: "))
          discount_rate = float(input("Enter the discount rate (as a percentage): "))
      except ValueError:
          print("Invalid input. Please enter numeric values for quantity, price, and discount rate.")
          continue

      discount_amount, discounted_price = compute_discount(quantity, price, discount_rate)
      print(f"Quantity: {quantity}, Price per Item: ${price:.2f}")
      print(f"Discount Amount: ${discount_amount:.2f}, Discounted Price: ${discounted_price:.2f}")

if __name__ == "__main__":
  main()
