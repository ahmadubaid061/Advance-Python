#getter and setter methods are used to access and modify the private attributes of a class
#suppose we have a class called Person with private attributes name and age and we want to access and modify these attributes outside the class then we can use getter and setter methods
class Person:
    def __init__(self,name,age):
        self.__name=name #this is a private attribute
        self.__age=age #this is also a private attribute

    def get_name(self): #this is a getter method to access the private attribute name
        return self.__name

    def get_age(self): #this is a getter method to access the private attribute age
        return self.__age

    def set_name(self,name): #this is a setter method to modify the private attribute name
        self.__name=name

    def set_age(self,age): #this is a setter method to modify the private attribute age
        self.__age=age  
p1=Person("John",30)
print(p1.get_name()) #this will print John      
print(p1.get_age()) #this will print 30
#now if we want to modify the name and age of the person we can use the setter methods
p1.set_name("Mike") #this will modify the name of the person to Mike
p1.set_age(35) #this will modify the age of the person to 35            