# we can also say it as list of list 

mylists=[[1,2,3],[4,5,6],[7,8,9]]

# printing usin for loop
for list in mylists:
    print("[ ",end=(''))
    for sublist in list:
        print(sublist,end=(" "))
    print(']')