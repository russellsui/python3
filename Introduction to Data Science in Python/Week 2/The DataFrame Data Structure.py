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
# 在 Series 中，index 是dict中(label,value)中的label，而在dataframe中，index是需要自己赋值的
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])
# 这就相当于在Dataframe中，列是可以直接用label调用的方式读取的而行是需要用loc函数的
print(df['Item Purchased'])
# 也可以对于两个维度同时进行选取，比如
df.loc['Store 1', 'Cost']
df.loc['Store 1']['Cost']
# select some columns from the table using slicing
df.loc[:,['Name','Cost']]
# drop some rows using drop function, like changing the df in its view,but does not change the original df
df.drop['Store 1']
# this dropping just changes a copy of the original dataframe so the original dataframe does not actually changes
copy_df = df.copy()
copy_df = copy_df.drop['Store 1']
# drop columns by using del function
del copy_df['Name']
copy_df
# adding columns to the dataframe just using the assignment
df['location']= None
df
