'''
The walrus operator (:=), introduced in Python 3.8, allows you to assign a value to a variable inside an expression.
'''
#----------------------------------------- without walrus operator
name = "Elizabeth"
# Step 1: Assign the value

name_length = len(name)

# Step 2: Use the value
if name_length > 5:
    print(f"That is a long name with {name_length} letters.")


#----------------------------------------- with walrus operator
name = "Elizabeth"

# Assigns name_length AND checks if it is > 5 at the same time
if (name_length := len(name)) > 5:
    print(f"That is a long name with {name_length} letters.")
