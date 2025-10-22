
# budget_tracker.py — Enhanced Budget Tracker
# Author: LaxmiPrasad Konduri
# Description: Track income and expenses with date, persistent CSV storage, monthly reports, and grouped bar charts for both income and expenses by category. Use interactively or via CLI for automation.

import argparse
from datetime import datetime
import os
import pandas as pd
import matplotlib.pyplot as plt

# Initialize empty DataFrame or load existing
CSV_PATH = os.path.join(os.path.dirname(__file__), 'data.csv')
columns = ['Date', 'Type', 'Category', 'Amount', 'Description']
if os.path.exists(CSV_PATH):
    try:
        data = pd.read_csv(CSV_PATH, parse_dates=['Date'])
    except Exception:
        data = pd.DataFrame(columns=columns)
else:
    data = pd.DataFrame(columns=columns)

def add_entry(entry_type, category=None, amount=None, description=None, date=None):
    """Add income or expense entry. Accepts optional parameters for non-interactive use."""
    global data
    if category is None:
        category = input("Enter category (e.g., Food, Rent, Salary): ")
    if amount is None:
        amount = float(input("Enter amount: "))
    else:
        amount = float(amount)
    if description is None:
        description = input("Enter a short description: ")
    if date is None:
        date = datetime.today().date()
    else:
        # accept YYYY-MM-DD or similar
        date = pd.to_datetime(date).date()

    data.loc[len(data)] = [pd.to_datetime(date), entry_type, category, amount, description]
    save_data()
    print(f"{entry_type} of ${amount:.2f} added under {category} on {date}.\n")

def save_data():
    """Persist the DataFrame to CSV."""
    try:
        data.to_csv(CSV_PATH, index=False)
    except Exception as e:
        print(f"Warning: failed to save data to {CSV_PATH}: {e}")

def view_summary():
    """Show balance and spending summary."""
    if data.empty:
        print("No entries yet.")
        return

    total_income = data[data['Type'] == 'Income']['Amount'].sum()
    total_expense = data[data['Type'] == 'Expense']['Amount'].sum()
    balance = total_income - total_expense

    print("\n----- Summary -----")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expense: ${total_expense:.2f}")
    print(f"Remaining Balance: ${balance:.2f}\n")

    plot_spending()

def plot_spending():
    """Plot both income and expenses by category as grouped bars."""
    if data.empty:
        print("No data to plot.")
        return
    grouped = data.groupby(['Category', 'Type'])['Amount'].sum().unstack(fill_value=0)
    # Ensure both columns exist for plotting
    for col in ['Income', 'Expense']:
        if col not in grouped.columns:
            grouped[col] = 0
    grouped = grouped[['Income', 'Expense']]
    grouped.plot(kind='bar', title='Income and Expenses by Category')
    plt.ylabel('Amount ($)')
    plt.tight_layout()
    plt.show()

def monthly_report(year=None, month=None):
    """Print a monthly report. If year/month are None, use current month."""
    if data.empty:
        print("No entries to report.")
        return

    df = data.copy()
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month

    if year is None or month is None:
        today = datetime.today()
        year = today.year if year is None else year
        month = today.month if month is None else month

    period = df[(df['Year'] == int(year)) & (df['Month'] == int(month))]
    if period.empty:
        print(f"No entries for {year}-{int(month):02d}.")
        return

    income = period[period['Type'] == 'Income']['Amount'].sum()
    expense = period[period['Type'] == 'Expense']['Amount'].sum()
    by_category = period[period['Type'] == 'Expense'].groupby('Category')['Amount'].sum()

    print(f"\n--- Monthly Report for {year}-{int(month):02d} ---")
    print(f"Income: ${income:.2f}")
    print(f"Expense: ${expense:.2f}")
    print(f"Net: ${income - expense:.2f}\n")
    if not by_category.empty:
        print("Expenses by category:")
        print(by_category.to_string())

def parse_args_and_run():
    parser = argparse.ArgumentParser(description='Budget Tracker')
    sub = parser.add_subparsers(dest='cmd')

    addp = sub.add_parser('add', help='Add an entry non-interactively')
    addp.add_argument('--type', required=True, choices=['Income', 'Expense'])
    addp.add_argument('--category', required=True)
    addp.add_argument('--amount', required=True)
    addp.add_argument('--description', default='')
    addp.add_argument('--date', default=None)

    reportp = sub.add_parser('report', help='Show monthly report')
    reportp.add_argument('--year', type=int)
    reportp.add_argument('--month', type=int)

    args = parser.parse_args()
    if args.cmd == 'add':
        add_entry(args.type, category=args.category, amount=args.amount, description=args.description, date=args.date)
    elif args.cmd == 'report':
        monthly_report(year=args.year, month=args.month)


def main():
    while True:
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_entry('Income')
        elif choice == '2':
            add_entry('Expense')
        elif choice == '3':
            view_summary()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        parse_args_and_run()
    else:
        main()
