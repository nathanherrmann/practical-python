# mortgage.py
#
# Exercise 1.7
import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

while principal > 0:
	principal = principal * (1+rate/12) - payment
	total_paid = total_paid + payment

print('Total paid:', locale.currency(total_paid, grouping=True))
