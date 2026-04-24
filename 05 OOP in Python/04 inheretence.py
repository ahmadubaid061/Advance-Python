#inheretence is what classes  classes are used for 
#due to inheretence we use methods of one class in other classes (child classes)
#Inheretence means passing of something from parents to offsprings
#in programming that something is the attributes and methods

#suppose we have a class called Animal and it has some attributes and methods and we want to use those attributes and methods in other classes like Dog and Cat then we can use inheretence
class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species

    def make_sound(self):
        if self.species=="Dog":
            return "Woof"
        elif self.species=="Cat":
            return "Meow"
        else:
            return "Unknown sound"

#now we can create classes for Dog and Cat that inherit from the Animal class
class Dog(Animal):
    def __init__(self,name):
        super().__init__(name,"Dog")

class Cat(Animal):
    def __init__(self,name):
        super().__init__(name,"Cat")    
    
#now we can create objects of the Dog and Cat classes and use the make_sound method which is inherited from the Animal class
dog1=Dog("Buddy")   
cat1=Cat("Whiskers")
print(dog1.name) #this will print Buddy
print(dog1.species) #this will print Dog
print(dog1.make_sound()) #this will print Woof
print(cat1.name) #this will print Whiskers
print(cat1.species) #this will print Cat
print(cat1.make_sound()) #this will print Meow
