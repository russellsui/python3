##### lambda function
my_function = lambda a,b,c:a+b
print(my_function(2,3,2))


####### Exercise 1
l = list(map(lambda x:x*x,range(20)))
print(l)

###### Exeercise 2
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson',
'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]

#option 1
for person in people:
    print(split_title_and_name(person) == (lambda person:person.split()[0]+
    ' '+person.split()[-1]))

#option 2
try:
    print(list(map(split_title_and_name, people)) == list(map(lambda person:person.split([0]
+' '+ person.split()[1],people))))

except:
    #list comprehension
    my_list = [number for number in range(100) if number%2 == 0]
    print(my_list)
