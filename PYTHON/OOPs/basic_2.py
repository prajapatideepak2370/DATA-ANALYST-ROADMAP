class student:
    def __init__(self, name, marks): #The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created.
        self.name = name  #The self parameter is a reference to the current instance of the class.
        self.marks = marks

    def get_avg(self):
        avg_score = 0
        n = len(self.marks)
        for val in self.marks:
            avg_score += val
        return avg_score/n
        

s1 = student("Deepak", [99, 98, 97, 12])
print("HII", s1.name, " your avg Score is:", s1.get_avg())

s1.name = "Sneha"  #change the name attr value is also execute
print("HII", s1.name, " your avg Score is:", s1.get_avg())