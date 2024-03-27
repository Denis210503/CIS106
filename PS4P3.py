Total_for_meal = float(input("Enter the total for the meal: "))
print("\n")
tip_15 = Total_for_meal * 0.15
tip_18 = Total_for_meal * 0.18
tip_20 = Total_for_meal * 0.20
tip_18 = round(tip_18, 2)

print("Total:", Total_for_meal)
print("Tip: ", '{0:.2f}'.format(tip_15))
print("Total with tip: ", Total_for_meal + tip_15)
print("\n")

print("Total:", Total_for_meal)
print("Tip: ", '{0:.2f}'.format(tip_18))
print("Total with tip: ", Total_for_meal + tip_18)
print("\n")

print("Total:", Total_for_meal)
print("Tip: ", '{0:.2f}'.format(tip_20))
print("Total with tip: ", Total_for_meal + tip_20)

