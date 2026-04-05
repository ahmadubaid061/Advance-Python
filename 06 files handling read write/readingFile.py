# we can access the folling by open() function
# mydetails=open("the file location","what you need to do like read,write,read+write")
# make sure to use farward slashes in the file address 
# the second argument of open() function means different purposes like 
'''
"r" means readonly
"w" means write only
"r+ means read and write
"a" means append
'''

mydetails=open("D:/python/Advance-Python/06 files handling read write/myfile.txt","r")
# print(mydetails.readlines()) # readlines() prints all the lines one by one
# a line once read cannnot be read again
# or i can also access a single line using readline() funciton
print(mydetails.readline()) #prints line #1 and moves to next
print(mydetails.readline()) #prints line #2 ....
print(mydetails.readline())
print(mydetails.readline())


# or i can loop through the whole file and print each line
# note: this will print only those lines that have not beeb read by the readilne() funciton before because all the lines have been read before in the file
for line in mydetails.readlines():
    print(line)
    print()
    
mydetails.close() #closes the file 