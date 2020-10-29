##Max Friedlander
##10-27-2020
##Basic Budgeting app.
""" Takes in user input and offers basic advice based on what type of budget you would like to have,
if your spending is extreme enough it puts out a warning and new budget. """
"""
TODO:
DONE: Use dictionaries to create spending and income categories
Create functions that populate category dictionaries based on user input until user is done. 
Use pre selected designations like housing, rent, food, etc.
Create pretty output of end budget, export to csv file?
Create risky and safe budget algorithm
Graphical output to better visualize the budget breakdown


"""

import re, math


def main():
    monthlyIncome = int(input('How much is your monthly income? '))
    monthlyExpense = int(input('How much are you spending every month? '))
    newBudget = budget(monthlyIncome, monthlyExpense, 'Safe')
    newBudget.updateBudget()
    budget.incomeCategories(newBudget)
    budget.spendingCategories(newBudget)
    print(newBudget.incomeCategories)
    print(newBudget.spendingCategories)


class budget():
    def __init__(self, monthlyIncome, monthlyExpense, budgetStyle):
        self.monthly = {}
        self.incomeCategories = {}
        self.spendingCategories = {}
        self.monthly['Monthly Income'] = monthlyIncome
        self.monthly['Monthly Expense'] = monthlyExpense
        self.budgetStyle = budgetStyle
        self.incomeCategories['W2'] = 0
        self.spendingCategories['Food'] = 0

    def incomeSources(self):
        pass

    def expenseSources(self):
        pass

    def updateBudget(self):
        choice = str(
            input('''Would you like a Safe or Risky budget?
                \nA riskier budget will allow you to spend more but you will have less leftover for a rainy day.
                \nWhereas a safer budget will afford you less big expenses, but greater peace of mind.
                \nBudget Selection: '''))
        if re.search('(S|s)afe', choice):
            print(
                'You have selected a Safe Budet style. Updating your account now.'
            )
            self.safeBudget()
        elif re.search('(R|r)isky', choice):
            print(
                'You have selected a Risky Budget style. Updating your account now.'
            )
            self.riskyBudget()
            self.budgetStyle = 'Risky'
        else:
            print(
                'You did not enter a valid budget stlye. You have defaulted to a safe style.'
            )
            self.safeBudget()

    def incomeCategories(self):
        pass

    def spendingCategories(self):
        pass

    def riskyBudget(self):
        pass

    def safeBudget(self):
        pass

    def displayBudget(self):
        pass


main()
