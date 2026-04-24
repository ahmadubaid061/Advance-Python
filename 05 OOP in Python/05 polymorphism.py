#poly means many and morphism means forms 
'''polymorphism means that a single class method can have ,multiple (in different forms) 
 implementation based on the context where they are used
 '''
 #method overloading is a type of polymorphism where a class has multiple methods with the same name but different parameters
 #method overriding is a type of polymorphism where a child class has a method with the same name and same parameters as a method in the parent class but with different implementation
#in python we cannot have method overloading but we can achieve it by using default parameters  
class Calculator:
    def add(self,a,b,c=0): #here c is a default parameter
        return a+b+c

# Example usage
calc = Calculator()
print(calc.add(5, 10))      # Output: 15
print(calc.add(5, 10, 15)) # Output: 30         

#polymorphism in child classes
class Animal:
    def make_sound(self):
        pass    

class Dog(Animal):
    def make_sound(self):
        return "Woof"       
    
class Cat(Animal):
    def make_sound(self):
        return "Meow"
# Example usage
dog = Dog()     
cat = Cat()
print(dog.make_sound()) # Output: Woof
print(cat.make_sound()) # Output: Meow
