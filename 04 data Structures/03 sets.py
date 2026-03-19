#sets are un_indexed data structure   which do not allow duplicate values
#their is no sequence in sets the items are stored at random position and cannot be retreived 
# by a specific index
#a set is initialized by curly braces {} unlike list [] and tuple ()
a={5,6,7,1,2,3,4,5}
print(type(a))   #<class 'set'>
print(a)       #{1, 2, 3, 4, 5, 6, 7} duplicates are ignored and the set is sorted   

#looping over a set  
#as sets are unindexed therefore cannot use use index for looping

for item in a:
    print(item)

#Note : 
#we cannot declare an empty set as "myset={}" because that will make it a dictionary 
#an empty set can be declared by using the set keyword
myset=set()
print(myset) #set()
myset.add(99)
print(myset)

union=myset.union(a)
print(union) #{1, 2, 99, 3, 4, 5, 6, 7}