import tkinter as tk
from tkinter import messagebox
import expense_tracker
import visualization
from datetime import datetime

def add_expense_gui():
    try:
        amount = float(entry_amount.get())
        category = entry_category.get()
        description = entry_description.get()
        if not category or not description:
            raise ValueError
        expense_tracker.add_expense(amount, category, description)
        messagebox.showinfo("Success", "Expense added successfully!")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid data.")

window = tk.Tk()
window.title("Personal Expense Tracker")

label_amount = tk.Label(window, text="Amount:")
label_amount.pack()
entry_amount = tk.Entry(window)
entry_amount.pack()

label_category = tk.Label(window, text="Category:")
label_category.pack()
entry_category = tk.Entry(window)
entry_category.pack()

label_description = tk.Label(window, text="Description:")
label_description.pack()
entry_description = tk.Entry(window)
entry_description.pack()

btn_add_expense = tk.Button(window, text="Add Expense", command=add_expense_gui)
btn_add_expense.pack()

btn_visualize_expense = tk.Button(window, text="Visualize by Category", command=visualization.visualize_by_category)
btn_visualize_expense.pack()

btn_trend = tk.Button(window, text="Show Spending Trend", command=visualization.visualize_spending_trend)
btn_trend.pack()

window.mainloop()
