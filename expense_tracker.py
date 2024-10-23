import csv
from datetime import datetime

file_name = 'expenses.csv'

def add_expense(amount, category, description):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])

def view_expenses():
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        return list(reader)

def calculate_total():
    total = 0
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            total += float(row[1])
    return total

def calculate_by_category():
    category_totals = {}
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            category = row[2]
            amount = float(row[1])
            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount
    return category_totals

def filter_expenses_by_date(start_date, end_date):
    expenses_in_range = []
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            date = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")
            if start_date <= date <= end_date:
                expenses_in_range.append(row)
    return expenses_in_range
