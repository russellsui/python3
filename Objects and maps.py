class Person:
    department = 'AAAAAAA'
    def set_name(self,newname):
        self.name = newname
    def set_location(self,newlo):
        self.location = newlo

####### map function
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
