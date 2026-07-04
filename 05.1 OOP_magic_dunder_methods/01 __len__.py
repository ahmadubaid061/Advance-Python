#len() function is used to return length of a list inside an object of a class

class Student:
    def __init__(self, name):
        self.name = name
        # Each student object has its own explicit list of subjects
        self.subjects = []  

    def enroll_subject(self, subject_name):
        self.subjects.append(subject_name)

    # Teach Python how to count the student's subjects
    def __len__(self):
        return len(self.subjects)

# 1. Create a student object
s1 = Student("Ubaid")

# 2. Add subjects to this specific student
s1.enroll_subject("Python Programming")
s1.enroll_subject("Data Structures")
s1.enroll_subject("Database Systems")

# 3. Call len() directly on the student object
print(f"{s1.name} is taking {len(s1)} subjects.")   #no need for telling which array
# Output: Ubaid is taking 3 subjects.
