num_tickets = int(input("Enter the number of concert tickets: "))

if num_tickets >= 25:
    price_per_ticket = 50
elif 10 <= num_tickets <= 24:
    price_per_ticket = 60
elif 5 <= num_tickets <= 9:
    price_per_ticket = 70
else:
    price_per_ticket = 75

total_cost = num_tickets * price_per_ticket

print("number of tickets:", num_tickets)
print("price per ticket: $", price_per_ticket)
print("total cost: $", total_cost)

