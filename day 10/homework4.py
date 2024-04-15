ticket_price = 10
ticket_count = int(input("Please enter how many tickets do you want to buy: "))

if ticket_count < 5:
    print(ticket_price * ticket_count)
else:
    discount = ticket_price - ((30 / 100) * ticket_price)
    print(discount * ticket_count)