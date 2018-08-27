#################### Indexing DataFrames ######################
# Now we wanna make new indexes for this DataFrames
df['country'] = df.index # using df.index to get all the country names and then set a new column to save it
df = df.set_index('Gold') # then after having stored the data of the original indexes, set the new indexes by set_index
df.head()
# Then we reset new index automatically using integers
df = df.reset_index()
df.head()
##################### Using new dataset
import pandas as pd
df = pd.read_csv('census.csv')
print(df.head())
# see what values does a column could take using unique function
print(df['SUMLEV'].unique()) # this will just return an array of unique values
# Then we wanna slicing wrt specific value of 'SUMLEV'
df = df[df['SUMLEV'] == 50]
print(df.head())
# if we just wanna keep some of the columns
columns_to_keep = ['RNETMIG2013','RNETMIG2014','RNETMIG2015']
df = df[columns_to_keep] # just keep the columns that selected
print(df.head())
df.reset_index()
print(df.head())
# while setting indexes, you could also use two factors like
df.set_index(['STNAME','CTYNAME'])
# now we wanna querying one element
df.loc['Michigan','Washtenaw county']
# querying several elements
df.loc[[('Michigan','Washtenaw County'),('Michigan','Wayne County')]]

###################### Exercise 1
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
print(df)
# the first level index is the original index 'Store 1',..., then the second level is  'Name'
df.set_index([df.index,'Name'])
df.index.names = ['Location','Name']
df = df.append(pd.Series({'Name':'Kevyn','Item Purchased':'Kitty Food','Cost': 3.00}))
print(df)
