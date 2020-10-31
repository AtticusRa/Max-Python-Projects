##Max Friedlander
##10-27-2020
##Basic Budgeting app.
""" Takes in user input and offers basic advice based on what type of budget you would like to have,
if your spending is extreme enough it puts out a warning and new budget. """
"""
TODO:
Create a Spreadsheet/csv that will be uploaded to google sheets. https://realpython.com/openpyxl-excel-spreadsheets-python/#writing-excel-spreadsheets-with-openpyxl
Add option to read and categorize transactions from one csv to another, aka from a bank statement to a budget document https://www.mint.com/mint-categories
Use pre selected designations like housing, rent, food, etc. https://www.quicken.com/blog/budget-categories
Create pretty output of end budget, export to csv file? 
Graphical output to better visualize the budget breakdown https://docs.google.com/spreadsheets/d/1w_tRBJ8ThfSyTctI_Mk2EnKLNbUZBTvjwijDtVLeW10/edit#gid=0
Organize expenses by category so they can fill into csv by category

Add valueError testing to user inputs for spending and income

1. Housing (25-35%)
2. Transportation (10-15)
3. Food (10-15)
4. Utilities (5-10)
5. Insurance (10-25)
6. Medical (5-10)
7. Saving, invest, debt (10-20)
-- non essential
8. Personal (5-10)
9. Rec + entertainment (5-10)
10. misc (5-10)


"""

import re, openpyxl


def main():
    name = input('Hi, what is your name? ')
    monthlyIncome = int(input('How much is your monthly income? '))
    monthlyExpense = int(input('How much are you spending every month? '))
    newBudget = budget(monthlyIncome, monthlyExpense, name)
    print(f'Hello {newBudget.name}')
    newBudget.incomeSources()
    newBudget.expenseSources()
    newBudget.displayBudget()


class budget():
    def __init__(self, monthlyIncome, monthlyExpense, name):
        self.monthly = {}
        self.incomeInput = []
        self.expenseInput = []
        self.incomeCategories = [
            'Paychecks', 'Investments', 'Returned Purchases', 'Bonuses',
            'Interest Income', 'Reimbursements', 'Rental Incomes'
        ]
        self.expenseCategories = [
            'Movies', 'Music', 'Streaming Services/Subscriptions', 'Groceries',
            'Eating Out/Delivery', 'Gifts/Donations', 'Health/Medical', 'Gas',
            'Rent', 'Auto Repair/Transportation', 'Pets', 'Utilities',
            'Debt & Interest Payments', 'Personal Care', 'Clothing',
            'Electronics/Virtual Products', 'Education Expenses', 'Phone',
            'Fees & Charges', 'Travel'
        ]
        self.monthly['Monthly Income'] = monthlyIncome
        self.monthly['Monthly Expense'] = monthlyExpense
        self.name = name

    def incomeSources(self):
        print(
            'Please enter the average amount your household earns from each item.\n'
        )
        for source in self.incomeCategories:
            self.incomeInput.append(int(input(source + ': ')))

    def expenseSources(self):
        print(
            'Please enter the average amount your household spends on each item every month. If you don\'t use this item, enter 0.\n'
        )
        for source in self.expenseCategories:
            self.expenseInput.append(int(input(source + ': ')))
        pass

    def displayBudget(self):
        res = '\n'.join(
            '{} {}'.format(x, y)
            for x, y in zip(self.incomeCategories, self.incomeInput))
        res2 = '\n'.join(
            '{} {}'.format(a, b)
            for a, b in zip(self.expenseCategories, self.expenseInput))
        print(f'Hello again, {self.name}, your income sources are: \n\n' + res)
        print('\n')
        print(f'Finally, {self.name}, your expenses are:\n\n' + res2)


if __name__ == '__main__':
    main()
