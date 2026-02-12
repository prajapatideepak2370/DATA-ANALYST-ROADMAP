class employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary
    def showDetails(self):
        print("Your role is", self.role)
        print("Your Department is", self.department)
        print("Your Salary is", self.salary)
    
class engineer(employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("SDE-2", "IT", 65900)

eng1 = engineer("Deepak", "20")
eng1.showDetails()