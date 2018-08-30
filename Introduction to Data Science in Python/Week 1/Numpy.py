import numpy as np
mylist = [1,2,3]
array1 = np.array(mylist)
array2 = np.array([[1,2,3],[4,5,6]])

# give the shape of array2
array2.shape()

# give a matrix of zeros,ones
array3 = np.zeros(2,3)
array4 = np.ones(3,5)

#diagonal matrix
array5 = np.eye(3)

#repear array
np.repeat([1,2,3],3)# this gives us array([1,1,1,2,2,2,3,3,3])

##########
### Operations
x = [1,2,3]
y = [4,5,6]
x * y
x ** 2

# dot production
x.dot(y)

# dtype denotes the type of the elements in an array
x = np.array([1,2,3,4,5],dtype = 'float')
# change dtype
x = x.astype('int')
# descriptive
x.max()
x.min()
x.mean()
x.std()
x.argmax()
x.argmin()

# arange function gives back an array from 0 to n-1
s = np.arange(13)
ss = s ** 2
print(ss)

#########################################################
######### Part II: Indexing/Slicing

x = np.array(range(10))
s = x ** 2 #take square of each element in x
(x,y,z) = (x[2],x[3],x[-1])
# first four elements
x[0:4]
# last four elements
x[-4:]
# from x[-5] go to the start by 2
x[-5::-2]
# conditional Indexing
x[x > 5] # gives the elements that is larger than 5
x[x > 5] = 5

# when we change the value of slices, the original array also changes
r = np.arange(36)
r.resize(6,6) #resize the 36 elements to be a 6*6 matrix
r2 = r(:3,:3) #r2 to be the upleft 3*3 block of r
r2[:] = 0 #set the entire r2 to be zeroes

# actually we could use the copy function to avoid changes for the original array
# when we wanna change the slicing array
old = np.array([[1,1,1],[2,2,1],[3,1,5]])
new = old.copy()
new[:,0] = 0
print(old) # in this case the old array remains unchanged

###########################################################################3
############ Part III: Interating over arrays
test = np.random.randint(0,10,(4,3)) #random integer ranges from 0 - 10 to form a 4*3 matrix
for row in test:
    print(row)
for i in range(len(test)):
    print(test[i])

# enumerate function could give us the row and index of the row
for i,row in enumerate(test):
    print('row',i,'is',row)
test2 = test ** 2

# iterate in both arrays, use zip function
for i,j in zip(test,test2):
    print(i,'+',j,'=',i+j)
    
