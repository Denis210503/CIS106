from forecast_functions import compute_next_month_sales

def main():
    while True:
        continue_program = input("Do you want to do this program (Yes or No)? ").strip().lower()
        if continue_program != 'yes':
            break

        last_name = input("Enter last name: ").strip()
        month = input("Enter month (e.g., Jan, Feb, etc.): ").strip()
        try:
            sales = float(input("Enter sales: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value for sales.")
            continue

        next_month_sales = compute_next_month_sales(month, sales)
        print(f"Last Name: {last_name}, Next Month's Sales Forecast: ${next_month_sales:.2f}")

if __name__ == "__main__":
    main()

