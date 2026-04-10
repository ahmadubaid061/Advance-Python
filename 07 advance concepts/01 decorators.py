''' is a function that takes a function then it creatre a new function inside its body called wrapper 
then returns the inside funciton
-- decorators are basically used for debuging to know if the funciton is executed or not 
'''
#suppose i have a funciton which prints hello

def sayHello():
    print("Hello")

sayHello()

'''
now suppose i want to print something before and after the execution of the funciton
that is where we need a decorator
-- decorator takes the funciton as a perimeter
-- then creates a new funciton called wrapper inside the body
-- inside the wrapper funciton we write what we want to print before execution of our function
-- then the funciton passed as argument is called 
-- then we write what we want to print after execution
-- the the wrapper function is returned by the decorator function 
-- and that's it when we call the decorator it the calls the wrapper which then calls the funciton we passed as argument 
'''

def decorator(func):
    def wrapper():
        print('I am gonna say Hello!') #we wanted to print this line before execution of the main funciton
        func() #here is the funciton called 
        print('I said Hello!')
    return wrapper

#now i am gonna call decorator and pass the say_hello funcitonas argument

myfun=decorator(sayHello) #returns the wrapper funciton which is stored in variable myfun
myfun() #this actually calls the wrapper function