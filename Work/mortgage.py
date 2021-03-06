# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000

month = 0
while principal > 0:
    pmt = min(principal * (1+rate/12), payment)

    month += 1
    principal = principal * (1+rate/12) - pmt
    total_paid = total_paid + pmt

    if extra_payment_start_month <= month <= extra_payment_end_month:
        principal -= extra_payment
        total_paid += extra_payment

    print(f"{month} {round(total_paid, 2)} {round(principal, 2)}")

print('Total paid', round(total_paid, 2))
print('Months', month)
