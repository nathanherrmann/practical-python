# mortgage.py
#
# Exercise 1.7
import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

principal = 500000.0
rate = 0.05
base_payment = 2684.11
extra_payment = base_payment + 1000
total_paid = 0.0
month = 1

while principal > 0:
    if month <= 12:
        principal = principal * (1+rate/12) - extra_payment
        total_paid = total_paid + extra_payment
    elif month > 12:
        principal = principal * (1+rate/12) - base_payment
        total_paid = total_paid + base_payment
    month = month + 1

print('Total paid:', locale.currency(total_paid, grouping=True))
