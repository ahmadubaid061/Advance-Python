# Python Special Methods
#1 printing an entire object using a special method called __str__
from operator import add


class Person: 
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self): #this is a special method that is called when we try to print an object of the class
        return f"Name: {self.name}, Age: {self.age}" #this will return a string representation of the object    
    
p1=Person("John",30)
print(p1) #this will print Name: John, Age: 30 because the __str__ method is called when we try to print the object p1
#2 adding two objects of a class using a special method called __add__
class Vector:   
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other): #this is a special method that is called when we try to add two objects of the class
        return Vector(self.x+other.x,self.y+other.y) #this will return a new object of the class Vector with the x and y values added together

v1=Vector(1,2)
v2=Vector(3,4)
v3=v1+v2 #this will call the __add__ method
print(v3.x,v3.y) #this will print 4 6   

#3 comparing two objects of a class using a special method called __eq__
class Point:    
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __eq__(self,other): #this is a special method that is called when we try to compare two objects of the class using the == operator
        return self.x==other.x and self.y==other.y #this will return True if the x and y values of both objects are equal and False otherwise
p1=Point(1,2)
p2=Point(1,2)

print(p1==p2) #this will print True because the __eq__ method is called when we try to compare the objects p1 and p2 using the == operator  

#4 getting the length of an object using a special method called __len__
class MyList:    
    def __init__(self,elements):
        self.elements=elements

    def __len__(self): #this is a special method that is called when we try to get the length of an object of the class using the len() function
        return len(self.elements) #this will return the length of the elements list

ml=MyList([1,2,3,4,5])
print(len(ml)) #this will print 5 because the __len__ method is called when we try to get the length of the object ml using the len() function  
#5 accessing an element of an object using a special method called __getitem__
class MyList:    
    def __init__(self,elements):
        self.elements=elements

    def __getitem__(self,index): #this is a special method that is called when we try to access an element of an object of the class using the indexing operator []
        return self.elements[index] #this will return the element at the specified index in the elements list

ml=MyList([1,2,3,4,5])
print(ml[0]) #this will print 1 because the __getitem__ method is called when we try to access the element at index 0 of the object ml using the indexing operator []

#6 setting an element of an object using a special method called __setitem__
class MyList:    
    def __init__(self,elements):
        self.elements=elements

    def __setitem__(self,index,value): #this is a special method that is called when we try to set an element of an object of the class using the indexing operator []
        self.elements[index]=value #this will set the element at the specified index in the elements list to the specified value
ml=MyList([1,2,3,4,5])
ml[0]=10 #this will call the __setitem__ method to set the element at index 0 of the object ml to 10
print(ml[0]) #this will print 10 because the __getitem__ method is  called when we try to access the element at index 0 of the object ml using the indexing operator []


#7 deleting an element of an object using a special method called __delitem__
class MyList:    
    def __init__(self,elements):
        self.elements=elements

    def __delitem__(self,index): #this is a special method that is called when we try to delete an element of an object of the class using the del keyword and the indexing operator []
        del self.elements[index] #this will delete the element at the specified index in the elements list
ml=MyList([1,2,3,4,5])
del ml[0] #this will call the __delitem__ method to delete the element at index 0 of the object ml
print(ml.elements) #this will print [2, 3, 4, 5] because the element at index 0 has been deleted from the elements list of the object ml

#8 calling a method of an object using a special method called __call__
class MyFunction:    
    def __init__(self,func):
        self.func=func

    def __call__(self,*args,**kwargs): #this is a special method that is called when we try to call an object of the class as a function
        return self.func(*args,**kwargs) #this will call the function stored in the func attribute with the specified arguments and keyword arguments       
    def add(a,b):
        return a+b      
my_add=MyFunction(add) #this will create an object of the MyFunction class with the add function stored in the func attribute
print(my_add(5,10)) #this will call the __call__ method to call the add function with the arguments 5 and 10 and print the result which is 15    

   