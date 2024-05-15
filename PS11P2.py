def display_names_and_scores(names, scores):
  print("Names and scores in original order:")
  for name, score in zip(names, scores):
      print(f"{name}: {score}")

def display_names_and_scores_reverse(names, scores):
  print("Names and scores in reverse order:")
  for name, score in zip(reversed(names), reversed(scores)):
      print(f"{name}: {score}")

def main():
  last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
  exam_scores = [85, 92, 88, 79, 95, 91, 76, 84, 89, 90]

  display_names_and_scores(last_names, exam_scores)
  print()
  display_names_and_scores_reverse(last_names, exam_scores)

if __name__ == "__main__":
  main()
