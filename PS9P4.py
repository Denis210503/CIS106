def get_pay_rate(job_code):
  if job_code == 'L':
      return 25
  elif job_code == 'A':
      return 30
  elif job_code == 'J':
      return 50
  else:
      return 0

def compute_gross_pay(hours_worked, pay_rate):
  if hours_worked > 40:
      regular_pay = 40 * pay_rate
      overtime_pay = (hours_worked - 40) * pay_rate * 1.5
      return regular_pay + overtime_pay
  else:
      return hours_worked * pay_rate

def main():
  total_gross_pay = 0
  employees = []

  while True:
      last_name = input("Enter last name (or 'done' to finish): ").strip()
      if last_name.lower() == 'done':
          break

      job_code = input("Enter job code (L, A, J): ").strip().upper()
      try:
          hours_worked = float(input("Enter hours worked: "))
      except ValueError:
          print("Invalid input. Please enter a numeric value for hours worked.")
          continue

      pay_rate = get_pay_rate(job_code)
      if pay_rate == 0:
          print("Invalid job code. Please enter L, A, or J.")
          continue

      gross_pay = compute_gross_pay(hours_worked, pay_rate)
      employees.append((last_name, gross_pay))
      total_gross_pay += gross_pay

  print("\nEmployee Gross Pay Summary:")
  for last_name, gross_pay in employees:
      print(f"Last Name: {last_name}, Gross Pay: ${gross_pay:.2f}")

  print(f"\nTotal Gross Pay for All Employees: ${total_gross_pay:.2f}")

if __name__ == "__main__":
  main()
