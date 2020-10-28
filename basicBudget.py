##Max Friedlander
##10-27-2020
##Basic Budgeting app.
""" Takes in user input and offers basic advice based on what type of budget you would like to have,
if your spending is extreme enough it puts out a warning and new budget. """

import re, math


def main():
    newBudget = budget.startAcct()
    newBudget.checkAcct()
    newBudget.updateBudget()


class budget():
    def __init__(self, monthlyIncome, monthlyExpense, spendingCategories,
                 incomeCategories):
        self.monthlyIncome = monthlyIncome
        self.monthlyExpense = monthlyExpense
        self.spendingCategories = spendingCategories
        self.incomeCategories = incomeCategories

    @classmethod
    def startAcct(cls):
        monthlyIncome = int(input('How much is your monthly income? '))
        monthlyExpense = int(input('How much are you spending every month? '))
        newBudget = budget(monthlyIncome, monthlyExpense, 1, 1)
        return newBudget

    def incomeSources(self):
        pass

    def expenseSources(self):
        pass

    def checkAcct(self):
        if self.monthlyExpense > self.monthlyIncome:
            print(
                'You are spending more than you are currently making. That\'s ok, let\'s suggest a good budget.'
            )
        else:
            print(r"You're not in the red. Let's make it even better.")

    def updateBudget(self):
        choice = str(input('Would you like a Safe or Risky budget? '))
        if re.search('(S|s)afe', choice):
            print('safe')
        elif re.search('(R|r)isky', 'choice'):
            print('risky')
        else:
            print('fail')


main()