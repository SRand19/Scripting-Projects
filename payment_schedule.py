def payment_schedule(price, down_payment_percent, interest_rate_percent, payment_percent):
    down_payment = price * down_payment_percent / 100
    balance = price - down_payment
    interest_rate = interest_rate_percent / 100 /12
    payment = payment_percent / 100 * (price - down_payment)

    print("Month\Balance\tInterest\tPrincipal\tPayment\tRemaining")
    for month in range(1, 13):
        interest = balance * interest_rate
        principal = payment - interest
        balance -= principal
        print("{}\t${:.2f}\t${:.2f}\t${:.2f}\t${:.2f}\t${:.2f}".format(month, balance, interest, principal, payment, balance))

price = float(input("Enter the purchase price: $"))
down_payment_percent = 10
interest_rate_percent = 12
payment_percent = 5

payment_schedule(price, down_payment_percent, interest_rate_percent, payment_percent)
