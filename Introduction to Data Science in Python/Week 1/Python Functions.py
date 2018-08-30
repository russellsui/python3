############# Python Functions
# original addition
x = 1
y = 1
print(x + y)
# using a python function
def add_numbers(x,y):
    return x + y
print(add_numbers(1,2))
# using default values
def add_numbers(x, y, z =None):
    if z == None:
        return x + y
    else:
        return x + y + z
add_numbers(1,2,3)
add_numbers(1,2)
