# writing file is of two types 
'''
1-creating new file
2-appending or overwriting the existing file
'''

# 1- overwriting the existing file
mydetails=open("D:/python/Advance-Python/06 files handling read write/myfile.txt","w")
mydetails.write("This is the new text\ni got a nick name Gull Khan") 
# this will actually change the txt file you can visit and see the content after running this code
# will we cannot  print mydetails in here because this is a write only file
print(mydetails.readable()) #returns false

# 2-  appending to the previous content
mydetails=open("D:/python/Advance-Python/06 files handling read write/myfile.txt","a")
mydetails.write("\nI love tea") #this adds a new line to the existing file

# 3-  creating new file
newdetails=open("D:/python/Advance-Python/06 files handling read write/newfile.txt","a")
#it creates a new file in the directory
newdetails.write("hello this is my new file")  #appends to the content of new file 
