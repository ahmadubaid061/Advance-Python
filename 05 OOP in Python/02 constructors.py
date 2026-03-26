#constructors are class methods used to initialize an object 
#a constructor is defind using the "__init__" keyword 
#we donot need to call constructors on an abject 
#as we create an object the constructor is called automatically

class student:
    
    #constructor
    def __init__(self,name,rollNo,gpa):
        self.name=name
        self.rollNo=rollNo
        self.gpa=gpa
        
    
#creating objects
student1=student("Ubaid",11,3.5) #the constructor is called from here
print(f"student Name: {student1.name} \n student rollNo: {student1.rollNo}\n student gpa: {student1.gpa}")
#changing an attribute value
student1.name="AlI"
print(f"student Name: {student1.name} \n student rollNo: {student1.rollNo}\n student gpa: {student1.gpa}")
