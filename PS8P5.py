def read_student_data(file_path):
  students = []
  with open(file_path, 'r') as file:
      lines = file.readlines()
      for i in range(0, len(lines), 3):
          last_name = lines[i].strip()
          district_code = lines[i + 1].strip()
          credits = int(lines[i + 2].strip())
          students.append((last_name, district_code, credits))
  return students

def calculate_tuition(students):
  total_tuition = 0
  for last_name, district_code, credits in students:
      if district_code == 'I':
          cost_per_credit = 250.00
      else:
          cost_per_credit = 500.00
      tuition = credits * cost_per_credit
      total_tuition += tuition
      print(f"Student: {last_name}, Credits: {credits}, Tuition Owed: {tuition:.2f}")
  return total_tuition

def main():
  file_path = 'student_data.txt'
  students = read_student_data(file_path)
  total_tuition = calculate_tuition(students)
  student_count = len(students)
  average_tuition = total_tuition / student_count if student_count > 0 else 0

  print(f"\nTotal Tuition Owed: {total_tuition:.2f}")
  print(f"Number of Students: {student_count}")

if __name__ == "__main__":
  main()
