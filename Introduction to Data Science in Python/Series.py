# The Series Data Structure
import pandas as pd
animals = ['Tiger','Bear','Wolf']
pd.Series(animals)
numbers = [1,2,3]
pd.Series(numbers)

# How do pandas deals with missing values?
animals = ['tiger','Bear',None]
pd.Series(animals) #it will gives the second item "None". So it seems as if 'None' is a values
numbers1 = [1,2,None]
pd.series(numbers1)#it will return the second item 'NaN'

# And we could also convert a dictionary to a Series
sports = {'Archery':'Bhutan','Golf':'Scotland','Soccer':'Japan'}
s = pd.Series(sports)
print(s) #this is similar with previous ones ,except for that now the indexes has changed to be the keys
s.index # return the indexes of the series

#This is actually the same if we construct the Series directly
s = pd.Series(['tiger','bear','lion'],index=['India','China','Japan'])
