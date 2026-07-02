#inheretence is what classes  classes are used for 
#due to inheretence we use methods of one class in other classes (child classes)
#Inheretence means passing of something from parents to offsprings
#in programming that something is the attributes and methods


# Parent class
class person:
    def __init__(self,name):
        self.__name=name
    
    def getName(self):  #getter method
        return self.__name
    
    def setName(self,name):  #setter method
        self.__name=name
        
     
#child class   
class student(person):
    def __init__(self,rollNo,name):
        super().__init__(name)  #parent class constructor must be called
        self.rollNo=rollNo
      
   
# child class 
class teacher(person):
    def __init__(self,dept, name):
        super().__init__(name)
        self.department=dept
    


p1=person("Gull Khan")
p2=student(11,"Ubaid")
p3=teacher('CS',"Bakhti Rahman")


#calling the getter method for private variables
print(p1.getName())
print(p3.getName()) #the getname method was inhereted from parent class

#setting the name of p2 using setter method
print("initially Name is: ",p2.getName()) #this prints the name before changing
p2.setName("Ahmad")  #setter method inhereted from parent class will change the name
print("After change Name is: ",p2.getName())
