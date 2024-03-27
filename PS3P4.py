make = input("Enter the brand of the car:")
model = input("Enter the model of the car:")
msrp_amount = float(input("Enter the MSRP amount of the car:"))
discount_percent1 = float(input("Enter the discount percent:"))
discount_percent2 = discount_percent1 / 100
discount_amount = msrp_amount * discount_percent2
discount_amount = round(discount_amount, 2)
final_price = msrp_amount - discount_amount
final_price = round(final_price, 2)

print("the original price for the", make, model, "is", msrp_amount, "dollars")
print("with a discount of %", discount_percent1,
      "the amount taken off the final price is", discount_amount)
print("the final discounted price is", final_price, "dollars")

