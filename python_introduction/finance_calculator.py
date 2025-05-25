monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses

Annual_interest = 0.05
projected_savings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))

print(f"Your monthly savings are: {monthly_savings}")
print(f"Your projected savings after one year, with interest, is: {projected_savings}")