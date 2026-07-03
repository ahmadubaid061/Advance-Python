'''suppose i want to call the decorator multiple times
 i will wrape the decorator inside another function'''
def repeat(n):
    def decorator(func):
        def wrapper(arg):      # for any no of args 'def wrapper(*args, **kwargs):'
            for i in range(n):
                print(f'reaptetion no: {i}')
                func(arg)
                print("funciton is finished!")
        return wrapper
    return decorator

# defining the function
@repeat(10)
def sayHello(name):
    print(f"Hello {name} How are you")


#now caling the function 
sayHello('Ubaid') #it will be called for 10 times
