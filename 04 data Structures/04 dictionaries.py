#python dictionaries is a specific data structure which stores data in the pairs
#each pair has a key and a value seperated by :
#dictionary is initialized by {} 

myDict={}  # this is how an empty dictionary is decalared 
myDict['Name']='Ubaid' #this adds a key "Name " with a value "Ubaid" to the dictionary

print(myDict) #{'Name': 'Ubaid'}

#retreiving all the keys ,all the values and all the items

print(myDict.keys()) # prints all the keys
print(myDict.values()) #prints all the values
print(myDict.items())  #prints all keys along with corresponding values

print(type(myDict)) #<class 'dict'>