part_number = input("Enter the part number: ")
quantity = int(input("Enter the quantity: "))

if part_number == "10" or part_number == "55":
    unit_cost = 1.00
elif part_number == "99":
    unit_cost = 2.00
elif part_number == "80" or part_number == "70":
    unit_cost = 3.00
else:
    unit_cost = 5.00

total_cost = quantity * unit_cost

print("Part number:", part_number)
print("cost per unit: $", unit_cost)
print("total cost: $", total_cost)
