def compute_scores(exam_scores):
  total_points = sum(exam_scores)
  average_score = total_points / len(exam_scores)
  return total_points, average_score

def main():
  while True:
      continue_program = input("Do you want to do this program (Yes or No)? ").strip().lower()
      if continue_program != 'yes':
          break

      last_name = input("Enter the student's last name: ").strip()
      try:
          exam_scores = [
              float(input("Enter score for Exam 1: ")),
              float(input("Enter score for Exam 2: ")),
              float(input("Enter score for Exam 3: "))
          ]
      except ValueError:
          print("Invalid input. Please enter numeric values for exam scores.")
          continue

      total_points, average_score = compute_scores(exam_scores)
      print(f"Student: {last_name}, Total Points: {total_points:.2f}, Average Score: {average_score:.2f}")

if __name__ == "__main__":
  main()
