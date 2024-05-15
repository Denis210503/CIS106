def compute_tuition(credit_hours, district_code):
  if district_code == 'I':
      return credit_hours * 250
  elif district_code == 'O':
      return credit_hours * 550
  else:
      return 0

def main():
  total_tuition = 0
  students = []

  while True:
      last_name = input("Enter student last name (or 'done' to finish): ").strip()
      if last_name.lower() == 'done':
          break

      try:
          credit_hours = int(input("Enter credit hours: "))
          district_code = input("Enter district code (I for In district, O for Out of district): ").strip().upper()
      except ValueError:
          print("Invalid input. Please enter numeric values for credit hours and valid district code.")
          continue

      tuition_owed = compute_tuition(credit_hours, district_code)
      if tuition_owed == 0:
          print("Invalid district code. Please enter 'I' for In district or 'O' for Out of district.")
          continue

      students.append((last_name, tuition_owed))
      total_tuition += tuition_owed

  print("\nStudent Tuition Summary:")
  for last_name, tuition_owed in students:
      print(f"Student: {last_name}, Tuition Owed: ${tuition_owed:.2f}")

  print(f"\nTotal Tuition Owed for All Students: ${total_tuition:.2f}")

if __name__ == "__main__":
  main()
