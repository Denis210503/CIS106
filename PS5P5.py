last_name = input("Enter your last name: ")
num_dependents = int(input("Enter the number of dependents: "))
gross_income = float(input("Enter your gross income: $"))


adjusted_gross_income = gross_income - (num_dependents * 12000)


if adjusted_gross_income > 50000:
    tax_rate = 0.20  
else:
    tax_rate = 0.10 


income_tax = adjusted_gross_income * tax_rate


if income_tax < 0:
    income_tax = 100

print("Last_name", last_name)
print("Gross income" , gross_income)
print("Number of dependents", num_dependents)
print("Adjusted gross income", adjusted_gross_income)
print("Income tax", income_tax)
