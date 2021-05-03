from array import *

salary = array('i',[+3990,4358,-9876,4523])
for i in range(4):
    print(salary[i])
print(type(salary[0])) #class of the value int/float/char etc
print(salary.buffer_info()) #buffer_info out the place where array stay and the length of array
print(salary.append(4000)) #to add a new count 4000 in the array
print(salary)
print(salary.remove(4358)) #to remove a value form the array
print(salary)
print(salary.reverse()) #print the array from opposite site
print(salary)
del salary[1]
print(salary) #to delet a value from the array using array position[1]

