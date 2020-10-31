#%%
class Test():
    sampleDict = {'1': True}

    def __init__(self, income, expense, value=None):
        self.monthly = {}
        self.monthly['Income'] = income
        self.monthly['Expense'] = expense
        self.value = value


t = Test(100, 900)
print(t.monthly)
t.monthly['Woke status'] = 'not woke'
print(t.monthly)
print(t.sampleDict)