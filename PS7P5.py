total_discount = 0

while True:
    choice = input("Do you want to continue? (Enter 'Yes' to continue): ")
    if choice.lower() != "yes":
        break

    quantity = int(input("Enter quantity of the item: "))
    price = float(input("Enter price of the item: "))

    extended_price = quantity * price

    if extended_price > 10000.00:
        discount_percent = 0.25
    else:
        discount_percent = 0.10

    discount_amount = extended_price * discount_percent
    total = extended_price - discount_amount

    print(f"Extended Price: {extended_price}")
    print(f"Discount Amount: {discount_amount}")
    print(f"Total: {total}")

    total_discount += discount_amount

    again = input("enter data for another item? (Enter 'Yes' to continue): ")
    if again.lower() != "yes":
        break

print(f"Total Discount: {total_discount}")
