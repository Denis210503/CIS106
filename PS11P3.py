def load_data(filename):
  names = []
  scores = []
  with open(filename, 'r') as file:
      for line in file:
          name, score = line.split()
          names.append(name)
          scores.append(int(score))
  return names, scores

def display_names_and_scores(names, scores):
  print("Names and scores in original order:")
  for name, score in zip(names, scores):
      print(f"{name}: {score}")

def display_names_and_scores_reverse(names, scores):
  print("Names and scores in reverse order:")
  for name, score in zip(reversed(names), reversed(scores)):
      print(f"{name}: {score}")

def display_highest_score(names, scores):
  high_var = -1
  high_index = -1
  for i, score in enumerate(scores):
      if score > high_var:
          high_var = score
          high_index = i
  print(f"Highest Score: {names[high_index]} with {high_var}")

def display_lowest_score(names, scores):
  low_var = 1000
  low_index = -1
  for i, score in enumerate(scores):
      if score < low_var:
          low_var = score
          low_index = i
  print(f"Lowest Score: {names[low_index]} with {low_var}")

def main():
  filename = 'students.txt'
  last_names, exam_scores = load_data(filename)

  display_names_and_scores(last_names, exam_scores)
  print()
  display_names_and_scores_reverse(last_names, exam_scores)
  print()
  display_highest_score(last_names, exam_scores)
  print()
  display_lowest_score(last_names, exam_scores)

if __name__ == "__main__":
  main()
