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


#5--------------------------------------union
newset={1,2,3,4,5,6,7}
newset2={1,3,5,7,9,11}
print(newset.union(newset2)) #prints the unio of both sets

#6-------------------------------------intersection
print(newset.intersection(newset2))

#7-------------------------------------issubset

set3={1,2,3}
print(set3.issubset(newset)) # returns true

#7-------------------------------------issuperset
print(newset.issuperset(set3)) #true

#8-------------------------------------isdisjoint
#returns true both sets havve no common element
print(newset.isdisjoint(set3)) #prints false because these sets are not disjoints 

set4={11,22,33}
print(set3.isdisjoint(set4)) #now this prints true

#9-------------------------------------difference
#returns values that are not prsesent in the other set
#simply set1 - set2

print(newset.difference(set3)) #{4, 5, 6, 7}

#10-----------------------------------clear
print(set4.clear()) #prints None

#11-------------------------------len()
print(len(set3)) #returns no of elements a set have
