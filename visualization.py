import matplotlib.pyplot as plt
from datetime import datetime
import expense_tracker

def visualize_by_category():
    category_totals = expense_tracker.calculate_by_category()
    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    plt.figure(figsize=(8, 8))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title("Expenses by Category")
    plt.show()

def visualize_spending_trend():
    expenses = expense_tracker.view_expenses()
    dates = []
    amounts = []

    for row in expenses:
        date = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")
        amount = float(row[1])
        dates.append(date)
        amounts.append(amount)

    cumulative_spending = [sum(amounts[:i+1]) for i in range(len(amounts))]

    plt.figure(figsize=(10, 6))
    plt.plot(dates, cumulative_spending, marker='o', linestyle='-', color='b')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Spending ($)')
    plt.title('Spending Trend Over Time')
    plt.grid(True)
    plt.show()
