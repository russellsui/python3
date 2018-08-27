######################## Missing Values #######################
import pandas as pd
df = pd.read_csv('log.csv')
print(df)
# Use df.fillna function to deal with the missing values
df = df.set_index('time')
print(df)
# first do some sorting, we have set the index to be time, then we sort then
# we sort the data by index, i.e. time
df = df.sort_index()
print(df)
# using hierarchy indexing to do the sorting
df = df.set_index([df.index,'user'])
print(df)
### there is several method to fillna, see the documentation for details
df = df.fillna(0)
print(df)
# also could give a dictionaries as a rule to filling the Na's
values = {'paused': 2.0, 'volumn': 1.0}
df = df.fillna(value = values)
print(df)

### DataFrame.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None, **kwargs)
