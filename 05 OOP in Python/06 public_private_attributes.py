#suppose there are some attributes in a class which we want to make private so that they cannot be accessed outside the class
#in python we can make an attribute private by adding double underscore before the attribute name
class Person:
    def __init__(self,name,age):
        self.__name=name #this is a private attribute
        self.__age=age #this is also a private attribute

    def get_name(self): #this is a getter method to access the private attribute name
        return self.__name

    def get_age(self): #this is a getter method to access the private attribute age
        return self.__age
p1=Person("John",30)
print(p1.get_name()) #this will print John      
print(p1.get_age()) #this will print 30
#now if we try to access the private attributes directly it will give an error
print(p1.__name) #this will give an error because __name is a private attribute 
print(p1.__age) #this will give an error because __age is a private attribute 
