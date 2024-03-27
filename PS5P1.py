quantity_of_item = int(input("Enter the quantity of item: "))
unit_price = 0
unit_price = unit_price + 3 
if quantity_of_item < 1000:
  unit_price += 2

extended_price = unit_price * quantity_of_item
tax = extended_price * 0.07
final_price = 0.07 * extended_price + extended_price

print("there are" , quantity_of_item , "items")
print("the unit price is $", unit_price)
print("the extended price is $", extended_price)
print("the tax is $", tax)
print("the final price is $", final_price)
