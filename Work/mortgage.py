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

month_count = 0

while principal > 0:
    month_count += 1
    principal = principal * (1+rate/12) - payment
    if (month_count >= extra_payment_start_month) and (month_count <= extra_payment_end_month):
        principal -=  extra_payment
        total_paid += extra_payment
    total_paid = total_paid + payment
    print(month_count, total_paid, principal)

print('Total paid', total_paid)
