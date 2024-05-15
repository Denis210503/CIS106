class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Employee Name: {self.name}, Salary: {self.salary}"

    def set_bonus_rate(self, bonus_rate):
        self.bonus_rate = bonus_rate

    def compute_bonus(self):
        return self.bonus_rate * self.salary

# Create an instance of Employee
employee = Employee("John smith", 50000)

# Display employee details
print(employee.get_details())

# Set a bonus rate for the employee and compute the bonus
employee.set_bonus_rate(0.1)  # 10% bonus rate
bonus = employee.compute_bonus()

# Display the bonus
print(f"Bonus for {employee.name}: {bonus}")
