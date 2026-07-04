#there are two types of variables (properties ) in classes 
#1- instance variables which are associated to a specific object and these variables are defined inside a constructor

#2- class variables are those which are shared by all the class objects and whose value is the same for all objects 
#class variables are defined before the constructor

class Student:
    no_of_Students=0  #class variable 
    
    def __init__(self,name,rollNo):
        self.name=name        #name and rollno are instance variables
        self.rollNO=rollNo
        Student.no_of_Students+=1    #the class varibale is increment when an object is created
    

#we can access the class variable directly using the class name 
print(f'No of Students in Class : {Student.no_of_Students}') 

#now as i create an object of the class the no_of_studnet becomes 1
s1=Student('Ubaid',11)

print(f'No of Students in Class : {Student.no_of_Students}') #1

#adding other two students
s1=Student('Ahmad',12)
s1=Student('ALI',13)
print(f'No of Students in Class : {Student.no_of_Students}')  #3