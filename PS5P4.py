appliance_name = input("Enter the name of the appliance: ")
appliance_cost = float(input("Enter the cost of the appliance: "))

if appliance_cost > 1000:
  warranty_cost = appliance_cost * 0.1
else:
  warranty_cost = appliance_cost * 0.05

total = appliance_cost + warranty_cost

print("the name of the appliance is", appliance_name)
print("the cost of the appliance is", appliance_cost)
print("the cost of the warranty is", warranty_cost)
print("the total cost is", total)
