# We could consider datafreame as a two-axises data array, rows are indexes, columns are labels
# Create a dataframe by combining the several Series
import pandas as pd
purchase_1 = pd.Series({'Name': 'Chris', 'Item Purchased': 'Dog Food','Cost': 22.5})
purchase_2 = pd.Series({'Name': 'Kevyn', 'Item Purchased': 'Kitty Kitter','Cost': 2})
purchase_3 = pd.Series({'Name': 'Vinod', 'Item Purchased': 'Bird Seed','Cost': 5.00})
df = pd.DataFrame([purchase_1,purchase_2,purchase_3],index = ['Store 1','Store 1','Store 2'])

# Querying a Dataframe by loc and labels
print(df.loc['Store 2'])
print(type(df.loc['Store 2'])) # returns Series
# But if there is two records have same index like this exp, they will both show up if we queries

####### Exercise 1 #########
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})

df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])
print(df['Item Purchased'])
