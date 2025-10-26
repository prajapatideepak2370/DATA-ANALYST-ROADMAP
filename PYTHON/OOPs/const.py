# CONSTRUCTOR 
class student:

    #Default Constructors 
    def __init__(self):
        pass

    # Parameterized Constructors
    def __init__(self, fullname, marks): # Create a constructor with parameter 
        self.name = fullname
        self.marks = marks
    print("Adding the new Student name in Database.")


s1 = student("Deepak", 78)
s2 = student("Sneha", 99)
print(s1.name, s1.marks)
print(s2.name, s2.marks)