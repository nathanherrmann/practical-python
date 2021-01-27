# mortgage.py
#
# Exercise 1.7
import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
total_paid = 0.0
month = 0

while principal > 0:
    month = month + 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

    if extra_payment_start_month <= month and month <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

    print(month, locale.currency(total_paid, grouping=True), locale.currency(principal, grouping=True))

print('Total paid:', locale.currency(total_paid, grouping=True))
print('Months', month)
