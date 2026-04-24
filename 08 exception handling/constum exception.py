#we can create a class for custom exceptions by inheriting from the built-in Exception class
class CustomException(Exception):   
    def __init__(self,message):
        self.message=message

    def __str__(self):
        return self.message 
    
try:
    raise CustomException("This is a custom exception") #this will raise a custom exception with the message "This is a custom exception"  
except CustomException as e:
    print(e) #this will print the message of the custom exception which is "This is a custom exception"     
        
         