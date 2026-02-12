#SINGLE INHERITANCE 

class car: # SINGLE PARENT CLASS
    @staticmethod
    def start():
        print("CAR IS STARTED@!!")
    @staticmethod
    def stop():
        print("CAR IS STOP!!")

#inheritance snytax is "class child_name(parent_name)"
class ToyotaCar(car):   # Single child  
    def __init__(self, Model_Name):
        self.Model_Name = Model_Name


c1 = ToyotaCar("Fortuner")
print(c1.start())
        
