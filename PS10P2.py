from room_functions import compute_square_footage, compute_gallons_needed

def main():
    while True:
        continue_program = input("Do you want to do this program (Yes or No)? ").strip().lower()
        if continue_program != 'yes':
            break

        try:
            length = float(input("Enter the length of the room: "))
            width = float(input("Enter the width of the room: "))
            height = float(input("Enter the height of the room: "))
        except ValueError:
            print("Invalid input. Please enter numeric values for length, width, and height.")
            continue

        square_footage = compute_square_footage(length, width, height)
        gallons_needed = compute_gallons_needed(square_footage)
        print(f"Square Footage: {square_footage:.2f} sq ft, Gallons of Paint Needed: {gallons_needed:.2f}")

if __name__ == "__main__":
    main()
