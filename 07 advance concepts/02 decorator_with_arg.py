'''now suppose i have funciton which takes some arguments'''

def decorator(func):
    def wrapper(arg):
        print(f'I am gonna call a funciton with argument {arg}....')
        func(arg)
        print("funciton is finished!")
    return wrapper

# defining the function
@decorator
def sayHello(name):
    print(f"Hello {name} How are you")


#now caling the function 
sayHello('Ubaid') #it will not just call the say hello func but the decorator function
