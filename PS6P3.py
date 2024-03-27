principle = float(input("Enter the principle amount of the CD: "))
years_to_maturity = int(input("Enter the years to maturity of the CD: "))

if principle > 100000:
    interest_rate = 0.06
elif 50000 <= principle <= 100000:
    if years_to_maturity == 10:
        interest_rate = 0.05
    elif years_to_maturity == 5:
        interest_rate = 0.04
    else:
        interest_rate = 0.02
else:
    interest_rate = 0.02

first_year_interest = principle * interest_rate

print("principle: $", principle)
print("interest rate:", interest_rate)
print("interest amount for the first yeat: $", first_year_interest)

