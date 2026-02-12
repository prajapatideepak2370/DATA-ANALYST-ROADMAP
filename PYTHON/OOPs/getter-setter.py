class employee:
    def __init__(self, salary):
        self.salary = salary

    @property
    def salary(self):
        return self._salary #getter
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            print("Invalid salary")
        else:
            self._salary = value

emp = employee(50000)
emp.salary = 60000 
print(emp.salary)