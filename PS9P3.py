def compute_mpg(miles, gallons):
  if gallons == 0:
      return 0.0
  else:
      return miles / gallons

def main():
  trips = []

  while True:
      destination = input("Enter the destination city (or 'done' to finish): ").strip()
      if destination.lower() == 'done':
          break

      try:
          miles = float(input("Enter miles traveled for the trip: "))
          gallons = float(input("Enter gallons used for the trip: "))
      except ValueError:
          print("Invalid input. Please enter numeric values for miles and gallons.")
          continue

      mpg = compute_mpg(miles, gallons)
      trips.append((destination, miles, mpg))

  print("\nTrip Summary:")
  for destination, miles, mpg in trips:
      print(f"Destination: {destination}, Miles: {miles:.2f}, MPG: {mpg:.2f}")

  print(f"\nTotal Number of Trips: {len(trips)}")

if __name__ == "__main__":
  main()
