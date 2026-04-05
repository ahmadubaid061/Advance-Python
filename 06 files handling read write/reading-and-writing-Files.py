'''
we can read and write a file at the same time using r+ argument in open function'''

newdetails=open("D:/python/Advance-Python/06 files handling read write/newfile.txt","r+")
newdetails.write("hello this is the updated content of the file")
print(newdetails.readlines())
print(newdetails.readable()) #true well it reads only the previous content 
print(newdetails.writable()) #true