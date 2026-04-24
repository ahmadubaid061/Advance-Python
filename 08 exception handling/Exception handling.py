# Exception Handling in Python
# used to handle errors that may occur during the execution of a program
# it is used with the 'try', 'except', and 'finally' statements in python

try:
    # code that may raise an exception
    with open("D:/python/Advance-Python/06 files handling read write/myfile.txt","r") as mydetails:
        print(mydetails.read())
except FileNotFoundError:
    # code to handle the specific exception
    print("File not found")
except Exception as e:
    # code to handle any other exception
    print("An error occurred:", e)
finally:
    # code that will always be executed, regardless of whether an exception occurred
    print("Execution completed")    

