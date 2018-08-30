############ Python Types and Sequences
type('this is a string')
type(32) # int
type(5.0) # float
# tuples are immutable, cannot reassign values
x = (1,'a',2,'b')
type(x) # tuple
x[2] = 3 # reassignment triggers traceback
# list are mutable
x = [1,2,3]
x.append(4) # add elements
# loop through list
for item in x:
    print(item)
# looping through while
i = 0
while i!= len(x):
    print(x[i])
    i += 1
# some easy operators
[1,2] + [3,4] # like append , not the addition in R
# slicing in a list
x = 'cannot'
x[1:2]
# last two letters
x[-2:-1]
x[2:] # the second char to the end
# some string operations
firstname = 'Russel'
lastname = 'Sui'
print(lastname + ' ' + firstname)
# repeat for several times
print(lastname * 3)
# check if is a substring
print('Ru' in firstname)
# using split function to split a string into a list of words
s1 = 'I am cool'
print(s1.split()[1])
# dictionary
x = {'key': 1, 'another':2}
# adding new keyvalues
x['anotherone'] = 3
# loop through the values
for number in x.values():
    print(number)
# loop through items:
for label,value in x.items():
    print(label)
    print(value)
# unpacking of a tuples, assign the value within a tuple into some vars
x = ('Russel','Sui')
first, last = x
print(first)
# But if we have different number of vars, there will be a traceback
