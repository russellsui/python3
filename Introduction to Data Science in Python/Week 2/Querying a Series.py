# First create a Series from dictionary
import pandas as pd
import numpy as np
sports = {'Archery':'Bhutan','Golf':'Scotland','Sumo':'Japan','Taekwondo':'South Korea'}
s = pd.Series(sports)
s.head() # gives you the top several records, like in R
print(s)

# Now we gonna query this Series
# First if we wanna query it by the order, we use s.iloc[]
print(s.iloc[3]) # remember here it is a bracket
print(s.loc['Golf']) # Now we are quering it by the index
# remember iloc and loc are attributes not objects so we use "[]" instead of '[]'
print(s[3]) # also ok
print(s['Golf']) # also ok

# Now doing some more operations
s = pd.Series([100, 120, 101 ,3])
total = 0
for item in s:
    total+= item
print(total)
#↑this is ok but not recommended it is too slow

total = np.sum(s)
print(total)
# if we use %timeit -n 100, we will find that using numpy function is faster

# how to iterate through all the items with in the series?
for label, value in s.iteritems():
    print(s.loc[label])
# s.iteritems()iterates through all the (index,value)pairs

# also we could use set_value to reset the values
s = pd.Series(np.random.randint(0,10000,10000))
for index,value in s.iteritems():
    s.set_value(index,value+2)
print(s.head())

### compare the two methods of changing values
### Method 1: By using iterations
#%%timeit -n 10
s = pd.Series(np.random.randint(0,10000,10000))
for label,value in s.iteritems():
    s.loc[label] = value+2 #其实相当于把(label,value)的pair取出来，然后加完2后用s.loc加回去

### Method 2: Using broadcast in numpy
#%%timeit -n 10
s = pd.Series(np.random.randint(0,10000,10000))
for label,value in s.iteritems():
    s += 2

### we could also adding new items into Series by loc function
s = pd.Series([1,2,3])
s.loc['animal'] = 'tiger'
print(s)

### we could alsp use append function to add two Series together
original_sports = pd.Series({'Archery':'Bhutan','Golf':'Scotland','Sumo':'Japan','Taekwondo':'South Korea'})
cricket_loving_countries = pd.Series(['Australia','Barbados','Pakistan','England'],index = ['Cricket','Cricket','Cricket','Cricket'])
all_countries = original_sports.append(cricket_loving_countries)
print(all_countries)
