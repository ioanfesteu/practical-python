# mortgage.py
#
# Exercise 1.7

print('Exercise 1.7')

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

while principal > 0:
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment

print('Total paid', total_paid)
print('\n')

# Exercise 1.8

"""
Suppose Dave pays an extra $1000/month for the first 12 months of the mortgage?
Modify the program to incorporate this extra payment and have it print the total amount paid along with the number of
months required.
When you run the new program, it should report a total payment of 929,965.62 over 342 months
"""

print('Exercise 1.8')

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

for _ in range(12):
    principal = principal * (1 + rate / 12) - (payment + 1000.0)
    total_paid = total_paid + (payment + 1000.0)

while principal > 0:
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment

print('Total paid', total_paid)
print('\n')

# Exercise 1.9

"""
Modify the program so that extra payment information can be more generally handled. Make it so that the user can set
these variables:

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
Make the program look at these variables and calculate the total paid appropriately.

How much will Dave pay if he pays an extra $1000/month for 4 years starting in year 5 of the mortgage?
"""

print('Exercise 1.9')

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
# extra_payment_start_month = (4 * 12) + 1  # starting of year 5
# extra_payment_end_month = extra_payment_start_month + (4 * 12)
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

month = 1
while principal > 0:
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment
    if extra_payment_start_month <= month <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

    month += 1

print(f'Total paid in {month} months: {total_paid}')
print('\n')

# Exercise 1.10

"""
Modify the program to print out a table showing the month, total paid so far, and the remaining principal.
The output should look something like this:
1 2684.11 499399.22
2 5368.22 498795.94
3 8052.33 498190.15
4 10736.44 497581.83
5 13420.55 496970.98
...
308 874705.88 3478.83
309 877389.99 809.21
310 880074.1 -1871.53
Total paid 880074.1
Months 310
"""

print('Exercise 1.10')

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
# extra_payment_start_month = (4 * 12) + 1  # starting of year 5
# extra_payment_end_month = extra_payment_start_month + (4 * 12)
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

month = 1
while principal > 0:
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment
    if extra_payment_start_month <= month <= extra_payment_end_month:
        principal -= extra_payment
        total_paid += extra_payment
    print(f'{month} {round(total_paid, 2)} {round(principal, 2)}')
    month += 1

print('\n')

# Exercise 1.11

"""
While you’re at it, fix the program to correct for the overpayment that occurs in the last month.
"""

print('Exercise 1.11')

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
# extra_payment_start_month = (4 * 12) + 1  # starting of year 5
# extra_payment_end_month = extra_payment_start_month + (4 * 12)
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

month = 1
while principal > 0:
    if payment >= principal:
        payment = principal
        principal -= payment
        total_paid += payment
        print(
            f'In month {month} principal is {round(principal, 2)} because we have paid a total of '
            f'{round(total_paid, 2)} with a payment of {round(payment, 2)}'
        )
        break
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment
    if extra_payment_start_month <= month <= extra_payment_end_month:
        principal -= extra_payment
        total_paid += extra_payment
    print(
        f'In month {month} principal is {round(principal, 2)} because we have paid a total of '
        f'{round(total_paid, 2)} with a payment of {round(payment, 2)}'
    )
    month += 1

print('\n')
