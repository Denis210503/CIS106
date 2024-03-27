item = input("Enter the item: (A OR B) : ")
quantity = int(input("enter a quantity : "))
unit_price = 0

if item == "A":
  unit_price = 10
else:
  unit_price = 20

extended_price = unit_price * quantity

print("item :", item)
print("unit price :", unit_price)
print("extended price :", extended_price)
