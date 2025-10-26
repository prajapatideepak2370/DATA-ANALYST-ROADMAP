class student:
    college_name = "USICT" 

    @staticmethod  # this staticmethod is used for without passing any self parameter/arguments 
    def hel():
        print("Hello Python World!!!@@!!")


    def __init__(self, name, marks): 
        self.name = name
        self.marks = marks
    print("Adding the new Student name in Database.")

    def welcome(self):  # Create a Method 
        print("Welcome Student,", self.name)

    def get_marks(self):
        return self.marks

print(student.college_name)
s1 = student("Deepak", 78)
print(s1.welcome())
print(s1.get_marks)
s2 = student("Sneha", 99)
print(s2.name, s2.marks)
print(student.hel())