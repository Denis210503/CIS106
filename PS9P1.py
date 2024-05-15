def compute_extended_price(quantity, price):
  ext_price = quantity * price
  if ext_price > 10000:
      discount_amount = ext_price * 0.10
  else:
      discount_amount = 0
  new_ext_price = ext_price - discount_amount
  return new_ext_price

def main():
  total_ext_price = 0
  continue_program = input("Do you want to do this program (Yes or No)? ").strip().lower()

  while continue_program == 'yes':
      try:
          quantity = int(input("Enter quantity: "))
          price = float(input("Enter price: "))
          ext_price = compute_extended_price(quantity, price)
          print(f"Quantity: {quantity}, Price: {price:.2f}, Extended Price: {ext_price:.2f}")
          total_ext_price += ext_price
      except ValueError:
          print("Invalid input. Please enter numeric values for quantity and price.")

      continue_program = input("Do you want to continue with this program (Yes or No)? ").strip().lower()

  print(f"Total Extended Price: {total_ext_price:.2f}")

if __name__ == "__main__":
  main()
