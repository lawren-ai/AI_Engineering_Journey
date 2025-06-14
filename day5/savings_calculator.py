def calculate_savings(income, expenses):
    amount_saved = income - expenses
    savings_rate = (amount_saved/income) * 100
    print(f"You saved {amount_saved} this month. ({savings_rate})")

def generate_report(name, income, expenses):
    print(f"Hello {name}")
    print(f"Monthly Income: ${income}")
    print(f"Total Expenses: ${expenses}")

    

name = input("What is your name?: ")
monthly_income = int(input("How much do you earn monthly?: "))
expense = int(input("How many expenses do you want to enter?: \n"))
expense_dict = {}
total_expenses = 0
while expense != 0:
    expense_name = input("Enter expense name: ")
    expense_cost = int(input("Enter expense cost: "))
    expense_dict[expense_name] = expense_cost
    expense -= 1
    total_expenses += expense_cost
generate_report(name, monthly_income, total_expenses)
calculate_savings(monthly_income, total_expenses)