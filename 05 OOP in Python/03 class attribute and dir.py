''' class attributes are the ones defined inside the classes and inhereted by all the 
objects(instances) of that class.
class attributes are not supposed to be initialized by a constructor theese are fixed 
value attributes

'''

class employee:
    company="Google" #class attribute
    
    def __init__(self,name,age):
        self.name=name   #instance attribute
        self.age=age

employee1=employee("Ubaid",22)
employee2=employee("Ali",25)

print(employee1.company)  # Output: Google
print(employee2.company)  # Output: Google

#dir() is a built in function that returns a list of all the attributes and methods of an object
print(dir(employee1))