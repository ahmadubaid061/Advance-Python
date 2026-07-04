#static method is like class method but it does not need the self or cls keyword

class student:
    def __init__(self,roll,marks):
        self.rollNo=roll
        self.marks=marks
        
    @staticmethod
    def isEligible_for_admission(marks):
        if marks>=40:
            return True 
        else:
            return False
        
#creating an object 
s1=student(11,50)
print(f"Eligibility : {student.isEligible_for_admission(s1.marks)}")


#we can also check the eligiblity of any other object or just by giving the marks 
#no need that the object should of class student

print(f"Eligiblity with marks 30 : {student.isEligible_for_admission(30)}")
print(f"Eligiblity with marks 70 : {student.isEligible_for_admission(70)}")
print(f"Eligiblity with marks 25 : {student.isEligible_for_admission(25)}")