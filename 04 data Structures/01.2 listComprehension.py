''' list comprehension is a easy way of writing a funciton in
 just a single a line to create a list

'''
# suppose i want create a list of first 10 multiples of 4

# table_of_4=[]
# for i in range (0,10):
#     table_of_4.append(i*4)

# print(table_of_4)

#i can write the same funciton only in one line

tableOf4=[i*4 for i in range(0,10)]
print(tableOf4)
