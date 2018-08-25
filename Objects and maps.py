class Person:
    department = 'AAAAAAA'
    def set_name(self,newname):
        self.name = newname
    def set_location(self,newlo):
        self.location = newlo

####### map function
store1 =[10,11,12,12,15]
store2 =[12,123,3214,5234]
cheapset = map(min,store1,store2)
print(type(cheapset))
