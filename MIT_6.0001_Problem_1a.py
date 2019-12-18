

annual_salary = float(input("Enter annual salary: "))
portion_saved = float(input("Enter portion saved: "))
total_cost = float(input("Enter total cost of dream house: "))

portion_down_payment = 0.25
current_savings = 0.0
r = 0.04
monthly_salary = annual_salary / 12
n = 0

while current_savings <= (total_cost * portion_down_payment):
    current_savings = current_savings + (monthly_salary * portion_saved) + (current_savings * r/12)
    n += 1

print(int(current_savings))
print("It will take " + str(n) + " months to save.")










