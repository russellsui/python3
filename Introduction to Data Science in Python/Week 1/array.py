import numpy as np
from numpy import array as ar
a = ar(range(10))
print(a)

b = np.zeros(3,dtype='int')
print(b)

c = np.ones(3,dtype = 'float')
print(c)

d = ar(range(10))
print(d)

e = np.random.randint(5,10,3)
print(e)

###############################################################
##########                                          ###########
##########           Now coming to slicing          ###########
##########                                          ###########
###############################################################

g = ar([[1,2,3,4],[5,6,7,8],[12,43,23,22]])
print(g)
print(g[2][-1])
