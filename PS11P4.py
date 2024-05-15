def load_data(filename):
  player_names = []
  batting_averages = []
  with open(filename, 'r') as file:
      for line in file:
          name, average = line.split()
          player_names.append(name)
          batting_averages.append(float(average))
  return player_names, batting_averages

def display_arrays(names, averages):
  print("Player Names and Batting Averages:")
  for name, average in zip(names, averages):
      print(f"{name}: {average:.3f}")

def search_player(names, averages, search_name):
  for name, average in zip(names, averages):
      if name.lower() == search_name.lower():
          print(f"Player: {name}, Batting Average: {average:.3f}")
          return
  print(f"Player with last name '{search_name}' not found.")

def main():
  filename = 'players.txt'
  player_names, batting_averages = load_data(filename)

  display_arrays(player_names, batting_averages)
  print()

  while True:
      search_name = input("Enter the player's last name to search (or 'done' to finish): ").strip()
      if search_name.lower() == 'done':
          break
      search_player(player_names, batting_averages, search_name)
      print()

if __name__ == "__main__":
  main()
