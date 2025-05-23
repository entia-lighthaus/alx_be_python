# finance_calculator.py

# Prompt user for monthly income and expenses
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project annual savings with 5% interest
annual_savings = monthly_savings * 12
projected_annual_savings = annual_savings + (annual_savings * 0.05)

# Output the results
print("\n--- Savings Summary ---")
print(f"Monthly Savings: ${monthly_savings:.2f}")
print(f"Projected Annual Savings (with 5% interest): ${projected_annual_savings:.2f}")
