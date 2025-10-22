
# 💰 Budget Tracker

## 🧩 Overview
Budget Tracker is a simple Python project to record income and expenses, calculate totals, and analyze spending patterns.  
It demonstrates how data analysis and business logic intersect — a step toward smarter personal finance.


## ⚙️ Features
- Add and categorize expenses and income (with date tracking)
- Automatically calculate balances
- Display spending summaries by category
- Visualize both Income and Expenses by category (grouped bar chart)
- Export and persist data to CSV (`data.csv`)
- Generate monthly reports (income, expenses, category breakdown)
- Use interactively or via command-line arguments (for automation)

## 🧰 Technologies
- Python 3
- pandas (for data management)
- matplotlib (for spending charts)

## 🧪 Run Instructions
1. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

2. Run interactively:
   ```bash
   python budget_tracker.py
   ```
   Follow the prompts to add income/expenses, view summary, and plot spending.
   
   Every time you select "View Summary" (option 3), a grouped bar chart will appear showing both Income and Expenses by category (if any data exists).

3. Use CLI mode (non-interactive):
   - Add an entry:
     ```bash
     python budget_tracker.py add --type Income --category Salary --amount 3000 --description "Paycheck"
     python budget_tracker.py add --type Expense --category Food --amount 45 --description "Lunch"
     ```
   - Generate a monthly report (current month by default):
     ```bash
     python budget_tracker.py report
     # Or for a specific month/year:
     python budget_tracker.py report --year 2025 --month 10
     ```

## 📦 Data Persistence
- All entries are saved to `data.csv` in the project directory.
- The script loads previous data automatically on startup.


## 📊 Example Output
```
--- Monthly Report for 2025-10 ---
Income: $3000.00
Expense: $45.00
Net: $2955.00
Expenses by category:
Food    45.0
```

When you select "View Summary" in interactive mode, you will see a grouped bar chart like this:

| Category | Income | Expense |
|----------|--------|---------|
| Salary   | 3000   |    0    |
| Food     |   0    |   45    |

This is visualized as a grouped bar chart for easy comparison.
