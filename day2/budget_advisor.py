monthly_income = int(input("How much do you earn monthly?:\n "))
monthly_rent = int(input("How much do you pay for rent monthly?: \n"))
monthly_food_expenses = int(input("How much do you spend on food monthly?: \n"))
monthly_transport_expenses = int(input("How much do you spend monthly on transport?: \n"))

total_expenses = monthly_food_expenses + monthly_rent + monthly_transport_expenses
balance = monthly_income - total_expenses

if balance > 0:
    print(f"You're saving ${balance} this month.")
elif balance == 0:
    print("You are breaking even. Watch your spending!")
else:
    print(f"You are overspending by {abs(balance)}. Consider reducing expenses.")