''' we can replace a word(string) in a sentence with another using replace function'''
paragraph='My name is Ubaid'
print(f"the original paragraph is: {paragraph}")
# suppose i want to change the name in the paragraph
newname='Shah Gul'

print(f"the new paragraph is: {paragraph.replace('Ubaid',newname)}")
# important to note that the replace does not modify the paragraph it just creates a new paragraph with the modified version
# if i now print the paragraph it will print the original one

print(f"the paragraph after replace  is: {paragraph}")

