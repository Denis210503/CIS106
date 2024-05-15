def display_names(names):
  print("Names in original order:")
  for name in names:
      print(name)

def display_names_reverse(names):
  print("Names in reverse order:")
  for name in reversed(names):
      print(name)

def main():
  last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
  display_names(last_names)
  print()
  display_names_reverse(last_names)

if __name__ == "__main__":
  main()
