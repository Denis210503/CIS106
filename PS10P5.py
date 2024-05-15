total = 0
tax = 0

def compute_total_and_tax(quantity, unit_price):
    global total, tax
    total = quantity * unit_price
    tax = total * 0.07
    return total, tax

def main():
    while True:
        continue_program = input("Do you want to do this program (Yes or No)? ").strip().lower()
        if continue_program != 'yes':
            break

        try:
            quantity = int(input("Enter the quantity: "))
            unit_price = float(input("Enter the unit price: "))
        except ValueError:
            print("Invalid input. Please enter numeric values for quantity and unit price.")
            continue

        compute_total_and_tax(quantity, unit_price)
        print(f"Total: ${total:.2f}, Tax: ${tax:.2f}")

if __name__ == "__main__":
    main()
