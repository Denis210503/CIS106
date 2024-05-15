total_interest = 0

while True:
    principle = float(input("Enter principle amount: "))
    rate = float(input("Enter interest rate (in percentage): "))

    print("Year\tBeginning Balance\tInterest\tEnding Balance")

    beginning_balance = principle
    for year in range(1, 6):
        annual_interest = principle * (rate / 100)
        ending_balance = principle + annual_interest

        total_interest += annual_interest

        print(f"{year}\t{beginning_balance:.2f}\t\t{annual_interest:.2f}\t\t{ending_balance:.2f}")

        principle = ending_balance
        beginning_balance = principle

    print(f"Accumulated Interest for 5 years: {total_interest:.2f}")

    choice = input("Do you want to enter principle and interest rate again?: ")
    if choice.lower() != "yes":
        break
