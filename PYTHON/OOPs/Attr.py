# CLASS & INSTANCE ATTRIBUTES
class student:
    college_name = "USICT" # Class Attribute
    name = "Default Name" # Class Attr
    def __init__(self, name, marks): 
        self.name = name  # Obj Attr > Class Attr 
        self.marks = marks
    print("Adding the new Student name in Database.")


s1 = student("Deepak", 78)
print(s1.name, s1.marks)
s2 = student("Sneha", 99)
print(s2.name, s2.marks)
print(student.college_name)  # Accessing Class Attribute using Class Name
print(s1.college_name)      # Accessing Class Attribute using Object also...