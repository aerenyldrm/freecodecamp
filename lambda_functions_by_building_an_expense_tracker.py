def AddExpense(expense, amount, category):
    expense.append({"amount": amount, "category": category})
def PrintExpense(expense):
    for component in expense:
        print(f"amount: {component['amount']}, category: {component['category']}")
def TotalExpense(expense):
    return sum(map(lambda x: x['amount'], expense))
def FilterExpenseCategory(expense, category):
    return filter(lambda x: x['category'] == category, expense)
def main():
    expense = []
    while True:
        print("\nEXPENSE TRACKER\n")
        print("1. Add an Expense")
        print("2. List Entire")
        print("3. Show Total")
        print("4. Filter by Category")
        print("5. Exit")
        choice = input("\nenter a number between 1 and 5 to proceed: ")
        if choice.isdigit():
            if choice == '1':
                amount = float(input("\nenter amount: "))
                category = input("\nenter category: ")
                AddExpense(expense, amount, category)
            elif choice == '2':
                print("\nENTIRE EXPENSE\n")
                PrintExpense(expense)
            elif choice == '3':
                print("\ntotal expense:", TotalExpense(expense))
            elif choice == '4':
                category = input("\nenter category to filter: ")
                print(f"\nexpense for the {category}:\n")
                expense_from_category = FilterExpenseCategory(expense, category)
                PrintExpense(expense_from_category)
            elif choice == '5':
                print("\nPROGRAM EXIT")
                break
            else:
                print("\nPLEASE ENTER A NUMBER BETWEEN 1 - 5 TO PROCEED")
        else:
            print("\nPLEASE ENTER A NUMBER BETWEEN 1 - 5 TO PROCEED")
main()