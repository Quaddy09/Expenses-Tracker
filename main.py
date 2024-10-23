import expense_tracker
import visualization
from datetime import datetime

def main():
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total")
        print("4. Calculate by Category")
        print("5. Visualize Expenses by Category")
        print("6. Show Spending Trend")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            expense_tracker.add_expense(amount, category, description)
            print("Expense added.")
        
        elif choice == '2':
            expenses = expense_tracker.view_expenses()
            for expense in expenses:
                print(expense)
        
        elif choice == '3':
            total = expense_tracker.calculate_total()
            print(f"Total Expenses: ${total:.2f}")
        
        elif choice == '4':
            category_totals = expense_tracker.calculate_by_category()
            for category, total in category_totals.items():
                print(f"{category}: ${total:.2f}")
        
        elif choice == '5':
            visualization.visualize_by_category()

        elif choice == '6':
            visualization.visualize_spending_trend()

        elif choice == '7':
            break

if __name__ == "__main__":
    main()
