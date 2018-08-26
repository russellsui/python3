# using bracket directly to get column datas,if it just a single column, will be looking like a Series
import pandas as pd
purchase_1 = pd.Series({'Name': 'Chris', 'Item Purchased': 'Dog Food','Cost': 22.5})
purchase_2 = pd.Series({'Name': 'Kevyn', 'Item Purchased': 'Kitty Kitter','Cost': 2})
purchase_3 = pd.Series({'Name': 'Vinod', 'Item Purchased': 'Bird Seed','Cost': 5.00})
df = pd.DataFrame([purchase_1,purchase_2,purchase_3],index = ['Store 1','Store 1','Store 2'])

costs = df['Cost']
costs
# using broadcasting to reassign values
costs += 2
costs
# And if we look at the original dataframe, the values are also changed as well
# reading data from csv files, just like R
df = pd.read_csv('olympics.csv')
df.head()# show the first several rows
# the following syntaxes will skip the first column of ordinal indexes and the first rows of Nans
df = pd.read_csv('olympic.csv', index_col = 0, skiprows = 1)
df.head()
# get the column names by using columns function
df.columns
# An example on renaming columns
for col in df.columns:
    if col[:2] == '01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace = True)
    if col[:2] == '02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace = True})
