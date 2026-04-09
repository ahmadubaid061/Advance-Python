class animal:
    def __init__(self,bio_class,mute):
        self.bio_class=bio_class
        self.sound=mute
    def make_sound(self,s):
        self.sound=s

class dog(animal): #this is a child class of animal
    def make_sound(self, s): #overrides the parent class method
        self.sound=s

animal1=animal("Mamalia","mio")
print(animal1.sound)

#updating sound
animal1.make_sound("bark")
print(animal1.sound) #now this will print bark
animal2=dog("mamalia","mute") #inherets the  parent class constructor
print(animal2.sound) #it will print the sound as mute 