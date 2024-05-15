def compute_square_footage(length, width, height):
  floor_and_ceiling = 2 * length * width
  two_walls_length_height = 2 * length * height
  two_walls_width_height = 2 * width * height
  total_square_footage = floor_and_ceiling + two_walls_length_height + two_walls_width_height
  return total_square_footage

def compute_gallons_needed(square_footage):
  coverage_per_gallon = 50
  gallons_needed = square_footage / coverage_per_gallon
  return gallons_needed
