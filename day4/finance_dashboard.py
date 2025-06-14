name = input("What is your name: ")
age = int(input("How old are you?: "))
monthly_income = int(input("What is your monthly income?: "))


expense = int(input("How man expenses do you want to enter?: \n"))
expense_dict = {}
total_expenses = 0
while expense != 0:
    expense_name = input("Enter expense name: ")
    expense_cost = int(input("Enter expense cost: "))
    expense_dict[expense_name] = expense_cost
    expense -= 1
    total_expenses += expense_cost
print(total_expenses)
print(max(expense_dict.items()))
amount_saved = monthly_income - total_expenses
print("amount saved: ", amount_saved)
print(sorted(expense_dict))