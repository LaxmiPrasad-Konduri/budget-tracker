```python
# budget_tracker.py — Simple Budget Tracker
# Author: LaxmiPrasad Konduri
# Description: Track income and expenses and visualize spending by category.

import pandas as pd
import matplotlib.pyplot as plt

# Initialize empty DataFrame
columns = ['Type', 'Category', 'Amount', 'Description']
data = pd.DataFrame(columns=columns)

def add_entry(entry_type):
    """Add income or expense entry."""
    category = input("Enter category (e.g., Food, Rent, Salary): ")
    amount = float(input("Enter amount: "))
    description = input("Enter a short description: ")
    global data
    data.loc[len(data)] = [entry_type, category, amount, description]
    print(f"{entry_type} of ${amount:.2f} added under {category}.\n")

def view_summary():
    """Show balance and spending summary."""
    total_income = data[data['Type'] == 'Income']['Amount'].sum()
    total_expense = data[data['Type'] == 'Expense']['Amount'].sum()
    balance = total_income - total_expense

    print("\n----- Summary -----")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expense: ${total_expense:.2f}")
    print(f"Remaining Balance: ${balance:.2f}\n")

    if not data[data['Type'] == 'Expense'].empty:
        plot_spending()

def plot_spending():
    """Plot expenses by category."""
    expenses = data[data['Type'] == 'Expense']
    summary = expenses.groupby('Category')['Amount'].sum()
    summary.plot(kind='bar', title='Expenses by Category')
    plt.ylabel('Amount ($)')
    plt.tight_layout()
    plt.show()

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
    main()
