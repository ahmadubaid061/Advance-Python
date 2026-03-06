#tuples are immutable index collection of elements
# used for speed 
# can be accessed by index
#denoted by ()
#cannot be mutated
tuple1=(1,2,3)
#i cannot write like tuple1[0]=2
#because tuple elements cannot be mutated

print(tuple1[0],tuple1[2])
print(tuple1)

#creating a tuple with single value
# tuple2=(5)  ❌
tuple2=(5,) # we need to put a , after the element

print(tuple2)