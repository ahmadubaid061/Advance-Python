'''
suppose i do not know the exact number arguments user is gonna pass so i make a list out it and then access them by indecs'''

# the * is used with the perimeter indecates multiple values 
def greet(*names):
    print(f"welcome {names}")

greet("ubaid","AHmad","Ali")

# i can also print the first or second or any indexed value instead of printing whole list
def greet2(*names):
    print(f"welcome {names[0]}")
# now if i pass ,multipl values only the first one is printed
greet2("ubaid","AHmad","Ali") 