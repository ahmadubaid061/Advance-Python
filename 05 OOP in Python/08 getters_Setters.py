
class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.__marks=marks
    
    #defining the marks getter function
    @property 
    def marks(self):
        return self.__marks
        # now i can access the marks from anywhere
        
    # setter for marks
    @marks.setter
    def marks(self,newMarks):
        self.__marks=newMarks
    

s1=Student('Ubaid',23,90)

print(s1)
# print(s1.__marks) #marks is private cannot be accessed there fore getter is used

#accessing marks using the getter 
print(f'Student marks are: {s1.marks}')


#reassigning new marks to the student using the setter function
s1.marks=100

print(f'Student marks after change are: {s1.marks}')
