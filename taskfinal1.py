import numpy as np
import pandas as pd

df = pd.read_csv('csv_1.csv')
income_total=df['Income'].sum()
expense_total=df['Expense'].sum()

print('sum of income ' +str(income_total))
print('sum of expenses ' +str(expense_total))
#difference
difference=(income_total)-(expense_total)
print(difference)
df1=df.drop(["Income","Date"],axis=1)
#summary
groupby_items=df1.groupby(['Items']).agg(['count','sum'])

print( (groupby_items))
