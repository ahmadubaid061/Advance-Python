#sets do not have indeces so we cannot retrieve a data in a regullar pattern like index vise but still
#set have alot of methods that we can on it
 #1 ---------------------------------adding element
 #set.add() adds an item only if the item is not already present
myset={1,2,3}
myset.add(5)
print(myset) #{1, 2, 3, 5}

#2------------------------------------ remove
#remove methods removes an item from a set 
#if the item was not found it returns an error
print(myset.remove(5)) #prints none as a the item is removed now
#print(myset.remove(5)) this will return error because 5 is not found in the set

#3--------------------------------------discard
#this also removes and item from the set but returns no error if the item was not found
print(myset.discard(5)) #none

#4--------------------------------------pop
#pop method removes a random item and returns it
print(myset.pop())


#5--------------------------------------
