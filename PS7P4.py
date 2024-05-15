total_gross_pay = 0
employee_count = 0

while True:
    choice = input("Do you want to continue? (Enter 'Yes' to continue): ")
    if choice.lower() != "yes":
        break

    last_name = input("Enter employee last name: ")
    hours_worked = float(input("Enter hours worked: "))
    rate_of_pay = float(input("Enter rate of pay: "))

    if hours_worked > 40:
        hours_over_40 = hours_worked - 40
        gross_pay = (40 * rate_of_pay) + (hours_over_40 * rate_of_pay * 1.5)
    else:
        gross_pay = hours_worked * rate_of_pay

    print(f"Employee Last Name: {last_name}, Gross Pay: {gross_pay}")

    total_gross_pay += gross_pay
    employee_count += 1

    again = input("enter data for another employee? (Enter 'Yes' to continue): ")
    if again.lower() != "yes":
        break

if employee_count > 0:
    average_pay = total_gross_pay / employee_count
    print(f"Total Gross Pay: {total_gross_pay}")
    print(f"Number of Employees: {employee_count}")
    print(f"Average Pay: {average_pay}")
else:
    print("No data entered.")
