############# Reading and Writing CSV files
# first we need to import csv
import csv
# first use with open('...csv') as file open the file
with open('athlete_events.csv') as file:
# and then use the csv.DictReader to convert the file into a dict type
    lines = csv.DictReader(file)
    list = list(lines)
# actually if we use a list() function to operate on a dictionary, it will return back
# a list, the elements of this list is some sublist, one for each record, this sublist
# is consist of some tuples, each tuple is a (key,value) pair of this record
# after making it a list, we print the first three records
print(list[:3])
print(len(list))
# we could also get the keys of a single record by
print(list[0].keys())
sum = 0
