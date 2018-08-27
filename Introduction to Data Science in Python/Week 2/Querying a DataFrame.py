# Boolean mask:
# Boolean mask is another similar dataframe that works on the original one
# The values in Boolean mask is either True or falseself.
# After opearing Boolean mask on dataframe, the element with a mask"True" remains
# while the element with a mask "False" got cut off

# First using broadcast to make a Boolean mask
df['gold'] > 0
# Now using where function to operate the Boolean mask onto the dataframe
only_gold = df.where(df['gold']>0)
only_gold.head()
only_gold['Gold'].count()# doing some aggregate function
df['Gold'].count()
# Drop the NaN
only_gold = only_gold.dropna()
only_gold.head()
# another way to query the positive values on 'Gold'
only_gold = df[df['Gold']>0]
only_gold.head()
# doing some more complicated querying using or, and operators
len(df[df['Gold']>0 | df['Gold.1']>0])
# this will returns the number of rows that has both a positive gold value and a positive
# gold.1 value, remember to use parenthesis
df[(df['Gold']>0) & (df['Gold.1'] == 0)]

##################### Exercise 1 #######################
import pandas as pd
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
# find the names who spend greater than $3.00
print(df[df['Cost']>3.00]['Name'])
