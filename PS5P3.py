number_of_books = int(input("Enter the number of books: "))
cost_per_book = int(input("Enter the cost per book: "))
total = number_of_books * cost_per_book
if total > 50:
  shipping_cost = 0
 
else:
  shipping_cost = 25

print("the total for the the order is", total ,"$")
print("the shipping and handling is", shipping_cost, "$")

