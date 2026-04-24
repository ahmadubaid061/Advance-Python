# Context Manager in file handling
# used to automatically close the file after its suite finishes, even if an exception is raised at some point.
# it is used with the 'with' statement in python  
with open("D:/python/Advance-Python/06 files handling read write/myfile.txt","r") as mydetails:
    print(mydetails.read()) #prints the content of the file 
# here we dont need to write mydetails.close() because the file is automatically closed after the with block is executed

# if we try to read the file after the with block is executed it will give an error because the file is closed
# print(mydetails.read()) #this will give an error because the file is closed       

#another example of context manager is when we want to zip two files together and write the content of one file to another file
import zipfile      
with zipfile.ZipFile("D:/python/Advance-Python/06 files handling read write/myzip.zip","w") as myzip:
    myzip.write("D:/python/Advance-Python/06 files handling read write/myfile.txt") #this will add the file to the zip file
# here we dont need to write myzip.close() because the zip file is automatically closed after the with block is executed

# we can also use context manager to handle multiple files at the same time
with open("D:/python/Advance-Python/06 files handling read write/myfile.txt","r") as mydetails, open("D:/python/Advance-Python/06 files handling read write/newfile.txt","w") as newdetails:
    content=mydetails.read() #reads the content of the first file
    newdetails.write(content) #writes the content to the second file    
# here we dont need to write mydetails.close() and newdetails.close() because both files are automatically closed after the with block is executed  

# we can also use context manager to handle files in a loop
filenames=["D:/python/Advance-Python/06 files handling read write/myfile.txt","D:/python/Advance-Python/06 files handling read write/newfile.txt"]
for filename in filenames:
    with open(filename,"r") as file:
        print(file.read()) #prints the content of each file in the loop
# here we dont need to write file.close() because the file is automatically closed after the with block is executed in each iteration of the loop

# we can also use context manager to handle files in a function
def read_file(filename):
    with open(filename,"r") as file:
        return file.read() #returns the content of the file
print(read_file("D:/python/Advance-Python/06 files handling read write/myfile.txt")) #prints the content of the file using the function
