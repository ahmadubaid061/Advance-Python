#class methods are specific methods used for two purposes 
#1- modify class varibales 
#2- alternative constructor

#suppose i have a class Student
class Student:
    class_name='CS123'
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    #1  suppose i want to change the name of class
    @classmethod
    def change_class_name(cls,newName):  #cls means class just as self keyword
        cls.class_name=newName
    
    #2 suppose i want to create a new studnet object but i only now name and date of birth
    #so then i will create an alternative constructor which takes name and data of birth
    
    @classmethod
    def from_dob(cls,name,dob):
        current_year=2026
        age=current_year-dob  #actually the dob should be only birthyear here
        
        return cls(name,age)
    

#creating a normal object and then printing it
s1=Student('Ubaid',24)
print(f'Student name is: {s1.name}')
print(f'Student age is: {s1.age}')
print(f'Class Name is: {s1.class_name}')        #here we can access the class variable with both studnet object and class name
print(f'Class Name is: {Student.class_name}')


#changing the class name
Student.change_class_name('New AI Class')
print(f'Class Name is: {s1.class_name}')        #here we can access the class variable with both studnet object and class name
print(f'Class Name is: {Student.class_name}')


#creating a second object with birth year
s2=Student.from_dob('Ahmad',2003)
print(f'Student name is: {s2.name}')
print(f'Student age is: {s2.age}')
print(f'Class Name is: {s2.class_name}')        