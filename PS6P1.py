quantity = int(input("Enter the number of widgets: "))

if quantity > 10000:
    price_per_unit = 10.00
elif 5000 <= quantity <= 10000:
    price_per_unit = 20.00
else:
    price_per_unit = 30.00

extended_price = quantity * price_per_unit
tax = extended_price * 0.07
total = extended_price + tax

print("the extended price is $", extended_price)
print("the tax amount is $", tax)
print("total is $", total)
