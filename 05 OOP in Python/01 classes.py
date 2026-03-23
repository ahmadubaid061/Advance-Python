#classes are blue prints or templates from which other object (instances) can be created
'''think of a student admission form , an empty form is a template that can be filled by 
any body who wants to register .
as soon as somebody fills the form then the form is no more a template now it is a specific object (instance ) of that form 

'''

#writing the class for student registeratoion
class student:
    #here comes the common variables that can be shared by all objects of this class
    recentQualification='FSc'
    
    #here comes the constructor( will be explained in next file)
    def __init__(self,name,marks,location): #the self keyword is necessary
        self.studentName=name
        self.studentMarks=marks
        self.studentCity=location
        
    def eligible(self):
        if(self.studentMarks>=50):
            print(f"Yes Mr/Mrs {self.studentName} You are Eligible for Admission!")
        else:
            print(f"Sorry to say, Mr/Mrs {self.studentName} You are not Eligible for Admission !")
            

#creating objects of the student class

student1=student("Ubaid",70,"Buner") #student 1 is now an object
student1.eligible()

student2=student("bakhti rahman",30,"swat")
student2.eligible()