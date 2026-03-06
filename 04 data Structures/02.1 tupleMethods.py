#tuples are mutable
#so do not have mush methods like lists

#1 count(x) we can count appearance of an element in a tuple
tuple1=(1,2,1,2,3,4,3,3,4,3)
print(tuple1.count(3)) #appearance of 3 = 4

#2 index(x) returns the first occurance index of an element
print(tuple1.index(2)) #1

#we can modify the tuples by converting it to a list then again reconverting to tuple
list1=list(tuple1)
list1[0]=5
tuple2=tuple(list1)
print(tuple2) # now we have 5 at index 0

# but the original tuple1 remains the same
print(tuple1)