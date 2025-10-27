#MULTI-LEVEL INHERITANCE 

class car: # PARENT CLASS
    @staticmethod
    def start():
        print("CAR IS STARTED@!!")
    @staticmethod
    def stop():
        print("CAR IS STOP!!")


class ToyotaCar(car):   # child class of Car and Parent class for Accessories  
    def __init__(self, Model_Name):
        self.Model_Name = Model_Name

class Accessories(ToyotaCar): #Child Class of ToyotaCar
    def __init__(self, Speaker, Headlight, Wrapping):
        self.Speaker = Speaker
        self.Headlight = Headlight
        self.Wrapping = Wrapping


c1 = ToyotaCar("Fortuner")
c1 = Accessories("JBL", "Lexus Headlight", "Premium Black")
print(c1.start())
print(c1.Headlight)