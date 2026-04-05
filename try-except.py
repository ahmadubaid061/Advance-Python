# try except is used for data validation in user input
''' suppose i expect a user input of integer value'''
# age=int(input("Please enter your age: "))
# print(age)

# but if the user enters a string instead of integer value the execution stops and returns an error 
# we do not want to stop the execution and to tell the user what wwent wrong 
# so
try:
    user_age=int(input("Please enter your age: "))
    print(user_age)
except:
    # if user enters a value that is not integer it will ne automatically catched by except and prints the excepts portion
    print("something went wrong with input")
finally:
    print("try except finished")
    

# note: we can i also use the  "ValueError" with except for checking values validation only
#  like 'except ValueError:'