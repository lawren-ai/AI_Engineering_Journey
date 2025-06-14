expense = int(input("How man expenses do you want to enter?: \n"))
expense_dict = {}
total_expense = []
total = 0
while expense != 0:
    expense_name = input("Enter expense name: ")
    expense_cost = int(input("Enter expense cost: "))
    expense_dict[expense_name] = expense_cost
    expense -= 1
    total += expense_cost
print(expense_dict)
print(f"${total}")

if total < 500: 
    print("Good control on spending!")
else:
    print("Watch your expenses!")
