item_price = float(input("Enter the price of the item: "))
item_discountpercent = float(input("Enter the discount percentage: % "))
new_price = item_price - item_price * item_discountpercent / 100
discount_price = item_price - new_price
print("the item has had a discount of ", discount_price)
print("The new price of the item is: ", new_price)

