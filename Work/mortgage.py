# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
total_months = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000


while principal > 0:
    monthlyPayment = payment

    if (
        total_months >= extra_payment_start_month
        and total_months <= extra_payment_end_month
    ):
        monthlyPayment += extra_payment

    newPrincipal = principal * (1 + (rate / 12))
    monthlyPayment = min(newPrincipal, monthlyPayment)
    principal = newPrincipal - monthlyPayment

    total_paid += monthlyPayment
    total_months += 1
    print(total_months, round(total_paid, 2), round(principal, 2))

print("Total paid", round(total_paid, 2))
print("Total Months", round(total_months, 2))
