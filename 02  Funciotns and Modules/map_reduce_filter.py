#1 The map() function applies a specific function to every item in a list

numbers = [1, 2, 3, 4]

# Using a lambda function to square each item
squared = map(lambda x: x ** 2, numbers)

print(list(squared))  # Output: [1, 4, 9, 16]
# ==============================================================================================

#2 The filter() function tests each element in a List with a function that returns True or False.
# suppose i want to find even numbers
evens = filter(lambda x: x % 2 == 0, numbers)

print(list(evens))  # Output: [2, 4, 6]

# ==============================================================================================
''' 
#3
Unlike map and filter, reduce() must be imported from the functools module. It applies a function cumulatively to the items, reducing the sequence to a single cumulative value.
'''

from functools import reduce

# Step 1: 1 * 2 = 2
# Step 2: 2 * 3 = 6
# Step 3: 6 * 4 = 24
product = reduce(lambda x, y: x * y, numbers)

print(product)  # Output: 24
