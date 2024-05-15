def compute_batting_average(hits, at_bats):
  if at_bats == 0:
      return 0.0
  else:
      return hits / at_bats

def main():
  num_players = 9
  players = []

  for i in range(num_players):
      last_name = input(f"Enter last name for player {i + 1}: ")
      hits = int(input(f"Enter number of hits for {last_name}: "))
      at_bats = int(input(f"Enter number of at-bats for {last_name}: "))
      batting_average = compute_batting_average(hits, at_bats)
      players.append((last_name, batting_average))

  print("\nPlayer Batting Averages:")
  for last_name, batting_average in players:
      print(f"Last Name: {last_name}, Batting Average: {batting_average:.3f}")

  print(f"\nTotal Number of Players Entered: {len(players)}")

if __name__ == "__main__":
  main()
