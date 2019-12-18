

annual_salary_org = float(input("Enter annual salary: "))

semi_annual_raise = 0.07
r = 0.04
portion_down_payment = 0.25
total_cost = 1000000.0
actual_down_payment = portion_down_payment * total_cost

portion_saved_high = 10000
portion_saved_low = 0
portion_saved = 0
current_savings = 0
n = 0
steps = 0

while abs(actual_down_payment - current_savings) >= 100:
    n = 0
    current_savings = 0
    steps += 1
    portion_saved = (portion_saved_high + portion_saved_low) / 2
    annual_salary = annual_salary_org
    monthly_salary = annual_salary / 12

    while n <= 35:
        current_savings = current_savings + (monthly_salary * (portion_saved/10000)) + (current_savings * r / 12)
        n += 1
        if n % 6 == 0:
            monthly_salary = monthly_salary + (monthly_salary * semi_annual_raise)

    if current_savings >= actual_down_payment:
        portion_saved_high = portion_saved
        #print("high")
    else:
        portion_saved_low = portion_saved
        #print("low")
    #print(steps)
    #print(portion_saved)
    if portion_saved == 10000:
        break

if portion_saved <= 9999:
    print(int(current_savings))
    print("Best savings rate: " + str(portion_saved/10000))
    print("Steps in bisection search: " + str(steps))
else:
    print("Not possible")










