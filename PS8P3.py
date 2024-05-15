def determine_bonus_rate(salary):
    if salary >= 100000.00:
        return 0.20
    elif salary >= 50000.00:
        return 0.15
    else:
        return 0.10

def read_employee_data(file_path):
    employees = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 2):
            last_name = lines[i].strip()
            salary = float(lines[i+1].strip())
            employees.append((last_name, salary))
    return employees

def calculate_bonuses(employees):
    total_bonus = 0
    for last_name, salary in employees:
        bonus_rate = determine_bonus_rate(salary)
        bonus = salary * bonus_rate
        total_bonus += bonus
        print(f"Employee: {last_name}, Salary: {salary:.2f}, Bonus: {bonus:.2f}")
    print(f"\nTotal Bonuses Paid Out: {total_bonus:.2f}")

def main():
    file_path = 'employee_data.txt'
    employees = read_employee_data(file_path)
    calculate_bonuses(employees)

if __name__ == "__main__":
    main()
