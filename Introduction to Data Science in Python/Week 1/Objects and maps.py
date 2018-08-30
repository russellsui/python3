############### Objects and maps
class Person:
    department = 'AAAAAAA'
    def set_name(self,newname):
        self.name = newname
    def set_location(self,newlo):
        self.location = newlo

# Realization of an object of class Person
person = Person()
person.set_name('Christopher Brooks')
person.set_location('North Carolina')
statement = '{} works in {}'
# still remember what we have learnt for strings? use string.format to auto filling
new_statement = statement.format(person.name,person.location)
print(new_statement)

####### map function,it will operate the map function on the every element of the latter objects
# map(function, iterable): returns an iterator that applies function to every item of iterable
store1 = [1,2,3,3,5]
store2 = [2312,4123,123123,1]
mape = map(min,store1,store2)
print(type(mape))

### Exercise
people = ['Dr. Christopher Brooks','Dr. Kevym Collins-Thompson','Dr. VG Vinod Vydiswaran'
,'Dr.Daniel Romero']

def split_title_and_name(person):
    words = person.split()
    return words[0]+words[1]

list(map(split_title_and_name,people))
