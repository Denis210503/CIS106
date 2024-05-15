def load_data(filename):
  employee_names = []
  salaries = []
  with open(filename, 'r') as file:
      for line in file:
          name, salary = line.split()
          employee_names.append(name)
          salaries.append(float(salary))
  return employee_names, salaries

def display_names_and_salaries(names, salaries):
  print("Employee Names and Salaries:")
  for name, salary in zip(names, salaries):
      print(f"{name}: ${salary:.2f}")

def display_names_reverse(names):
  print("Employee Names in Reverse Order:")
  for name in reversed(names):
      print(name)

def find_highest_salary(names, salaries):
  highest_salary = max(salaries)
  highest_index = salaries.index(highest_salary)
  print(f"Highest Salary: {names[highest_index]} with ${highest_salary:.2f}")

def sum_and_display_total_salaries(salaries):
  total_salaries = sum(salaries)
  print(f"Total of All Salaries: ${total_salaries:.2f}")

def search_employee(names, salaries, search_name):
  for name, salary in zip(names, salaries):
      if name.lower() == search_name.lower():
          print(f"Employee: {name}, Salary: ${salary:.2f}")
          return
  print(f"Employee with last name '{search_name}' not found.")

def main():
  filename = 'employees.txt'
  employee_names, salaries = load_data(filename)

  display_names_and_salaries(employee_names, salaries)
  print()

  display_names_reverse(employee_names)
  print()

  find_highest_salary(employee_names, salaries)
  print()

  sum_and_display_total_salaries(salaries)
  print()

  while True:
      search_name = input("Enter the employee's last name to search (or 'done' to finish): ").strip()
      if search_name.lower() == 'done':
          break
      search_employee(employee_names, salaries, search_name)
      print()

if __name__ == "__main__":
  main()
